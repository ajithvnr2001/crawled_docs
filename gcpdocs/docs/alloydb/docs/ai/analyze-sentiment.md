---
url: https://docs.cloud.google.com/alloydb/docs/ai/analyze-sentiment/
title: Analyze text sentiment \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:37:54.871464+00:00
---

# Analyze text sentiment  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/analyze-sentiment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Analyze text sentiment Stay organized with collections  Save and categorize content based on your preferences. 

The `ai.analyze_sentiment` function is a built-in AlloyDB AI tool that classifies the sentiment of text as positive, negative, or neutral. By embedding this capability directly into the database, AlloyDB for PostgreSQL lets you apply Gemini language understanding to unstructured enterprise data in real time by using SQL—supporting single-string analysis, scalar function acceleration, and array-based or cursor-based batch processing across thousands of rows without complex Extract, Transform, and Load (ETL) pipelines.

You can use `ai.analyze_sentiment` to classify unstructured product reviews and customer feedback or analyze social media mentions to gauge brand perception.

**Note:** The `ai.analyze_sentiment` function is supported on PostgreSQL version 17 and later. AlloyDB pre-registers several Gemini models by default; for the full list, see [Pre-registered Gemini Enterprise Agent Platform models](https://docs.cloud.google.com/alloydb/docs/reference/supported-ai-models#pre-registered-models). To use another model, register the model endpoint first. For more information, see [Use a Gemini model that's supported in your region](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators#use-gemini-model) and [Register and call remote AI models using model endpoint management](https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint).

## Before you begin

Make sure that you meet the following requirements before you use the `ai.analyze_sentiment` function.

**Note:** AlloyDB doesn't charge for AI function calls. However, when you call Agent Platform, third-party, or self-hosted models and services (such as for hybrid search) from your database, the model or infrastructure provider charges you directly. For more information about Agent Platform costs, see [Pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing).

### Enable the extension

To use the `ai.analyze_sentiment` function, configure permissions, install or update the `google_ml_integration` extension, and enable the [`google_ml_integration.enable_ai_query_engine`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#google_ml_integration_enable_ai_query_engine) flag.

  1. Ensure that your AlloyDB instance has the required Identity and Access Management permissions to call Agent Platform endpoints. For more information, see [Configure user access to Agent Platform models](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).

  2. Verify that your `google_ml_integration` extension is version 1.6.4 or later. You can check the installed version by running the following command:



    
    
       SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
    

If the extension isn't installed or is an earlier version, install and update it by running the following commands:
    
    
       CREATE EXTENSION IF NOT EXISTS google_ml_integration;
       ALTER EXTENSION google_ml_integration UPDATE;
    

  1. Enable the [`google_ml_integration.enable_ai_query_engine`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#google_ml_integration_enable_ai_query_engine) flag for the current session or for the entire database. To enable the flag for your current session, run the following command:
         
         SET google_ml_integration.enable_ai_query_engine = 'on';
         

This change doesn't require a database restart. The default value of this flag is `on`.




### Create an example table

To follow the sentiment analysis examples in this document, create a table and populate it with the following movie reviews:
    
    
    CREATE TABLE IF NOT EXISTS reviews (
        id INT PRIMARY KEY,
        review_content TEXT
    );
    
    INSERT INTO reviews (id, review_content) VALUES
    (1, 'This movie is very good'),
    (2, 'The actors play the parts well'),
    (3, 'I like the music in this film'),
    (4, 'The story is easy to follow'),
    (5, 'Many people will enjoy this show'),
    (6, 'The film is too long'),
    (7, 'I do not like the ending'),
    (8, 'This movie is very boring'),
    (9, 'The story is okay'),
    (10, 'Some parts are fine');
    

## Analyze sentiment of a single string

To evaluate the sentiment of a single text input, use the scalar version of `ai.analyze_sentiment`. For each input, the function returns a sentiment classification of `positive`, `negative`, or `neutral`.

The function signature for the scalar version of `ai.analyze_sentiment` is as follows:
    
    
    CREATE OR REPLACE FUNCTION ai.analyze_sentiment(
      input TEXT,
      model_id VARCHAR(100) DEFAULT NULL)
    RETURNS TEXT
    

Use the following syntax to call the scalar function:
    
    
    SELECT ai.analyze_sentiment(
      input => 'TEXT_CONTENT',
      model_id => 'MODEL_ID' -- Optional. The default value is gemini-3.5-flash-lite.
    );
    

Replace the following:

  * `TEXT_CONTENT`: The text string to analyze.
  * `MODEL_ID`: Optional. The ID of the model to use. If omitted, the function uses the model specified by the `google_ml_integration.default_llm_model` flag, which defaults to `gemini-3.5-flash-lite`.



The following examples show different ways to call the scalar function on a single string:
    
    
    SELECT ai.analyze_sentiment('I am feeling joyful today');
    
    SELECT ai.analyze_sentiment(input => 'I am feeling joyful today');
    
    SELECT ai.analyze_sentiment(
      input => 'I am feeling joyful today',
      model_id => 'gemini-3.5-flash-lite'
    );
    

These queries return `positive`.

The following example performs row-level sentiment analysis on text data stored in the `reviews` table. The `SELECT` query applies the `ai.analyze_sentiment` function to the `review_content` column for each row in the table and returns its calculated sentiment (`positive`, `negative`, or `neutral`):
    
    
    -- Row-level sentiment analysis
    SELECT id, ai.analyze_sentiment(review_content) FROM reviews ORDER BY id;
    

The following is the example output:
    
    
     id | analyze_sentiment
    ----+-------------------
      1 | positive
      2 | positive
      3 | positive
      4 | positive
      5 | positive
      6 | negative
      7 | negative
      8 | negative
      9 | neutral
     10 | neutral
    

### Accelerate scalar functions with AI Function Acceleration

AI Function Acceleration (AIFA) speeds up scalar function execution by automatically grouping inputs into batches instead of processing them individually. You can enable AIFA for scalar functions using Grand Unified Configuration (GUC) settings to reduce overhead and improve query performance. For more information about enabling and configuring AIFA, see [Accelerate performance for queries with AI functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-ai-queries).

## Analyze sentiment in batches

For better performance on larger datasets, use the array-based version of the function to process multiple strings in a single call.

The function signature for the array-based version of `ai.analyze_sentiment` is as follows:
    
    
    CREATE OR REPLACE FUNCTION ai.analyze_sentiment(
      inputs TEXT[],
      batch_size INT DEFAULT NULL,
      model_id VARCHAR(100) DEFAULT NULL)
    RETURNS TEXT[]
    

Use the following syntax to call the array-based function:
    
    
    SELECT ai.analyze_sentiment(
      inputs => ARRAY['TEXT_1', 'TEXT_2'],
      batch_size => BATCH_SIZE, -- Optional. The default value is 10.
      model_id => 'MODEL_ID' -- Optional. The default value is gemini-3.5-flash-lite.
    );
    

Replace the following:

  * `TEXT_1`, `TEXT_2`: The text strings to analyze as elements of a `TEXT[]` array.
  * `BATCH_SIZE`: Optional. The number of inputs to process per batch. The default value is `10`.
  * `MODEL_ID`: Optional. The ID of the model to use. If omitted, the function uses the model specified by the `google_ml_integration.default_llm_model` flag, which defaults to `gemini-3.5-flash-lite`.



The following example passes an array of strings directly to `ai.analyze_sentiment`:
    
    
    SELECT ai.analyze_sentiment(
      ARRAY[
        'I am feeling joyful today',
        'I am feeling sad today',
        'what is the capital of India ?'
      ]
    );
    

The following is the example output:
    
    
    {positive,negative,neutral}
    

The following example aggregates rows from the `reviews` table into an array and analyzes the sentiment of the reviews in a batch:
    
    
    WITH sentiment_results AS (
      SELECT
        ARRAY_AGG(id ORDER BY id) AS ids,
        ai.analyze_sentiment(
          inputs => ARRAY_AGG(review_content ORDER BY id),
          batch_size => 10
        ) AS sentiments
      FROM reviews
    ),
    correlated_results AS (
      SELECT ids[i] AS id, sentiments[i] AS sentiment
      FROM sentiment_results,
      generate_series(1, array_length(ids, 1)) AS i
    )
    SELECT reviews.id, reviews.review_content, correlated_results.sentiment AS sentiment
    FROM reviews
    JOIN correlated_results ON reviews.id = correlated_results.id
    ORDER BY reviews.id;
    

The following is the example output:
    
    
     id |          review_content          | sentiment
    ----+----------------------------------+-----------
      1 | This movie is very good          | positive
      2 | The actors play the parts well   | positive
      3 | I like the music in this film    | positive
      4 | The story is easy to follow      | positive
      5 | Many people will enjoy this show | positive
      6 | The film is too long             | negative
      7 | I do not like the ending         | negative
      8 | This movie is very boring        | negative
      9 | The story is okay                | neutral
     10 | Some parts are fine              | neutral
    

## Analyze sentiment using cursors

The cursor-based function processes large datasets efficiently because it streams data through the AI model in manageable batches without requiring all of the data to be loaded into memory at once.

The function signature for the cursor-based version of `ai.analyze_sentiment` is as follows:
    
    
    CREATE OR REPLACE FUNCTION ai.analyze_sentiment(
      input_cursor REFCURSOR,
      batch_size INT DEFAULT NULL,
      model_id VARCHAR(100) DEFAULT NULL)
    RETURNS REFCURSOR
    

Use the following syntax to call the cursor-based function:
    
    
    SELECT ai.analyze_sentiment(
      input_cursor => INPUT_CURSOR,
      batch_size => BATCH_SIZE, -- Optional. The default value is 10.
      model_id => 'MODEL_ID' -- Optional. The default value is gemini-3.5-flash-lite.
    );
    

Replace the following:

  * `INPUT_CURSOR`: A `REFCURSOR` that points to a query returning a single `TEXT` column to analyze.
  * `BATCH_SIZE`: Optional. The number of inputs to process per batch. The default value is `10`.
  * `MODEL_ID`: Optional. The ID of the model to use. If omitted, the function uses the model specified by the `google_ml_integration.default_llm_model` flag, which defaults to `gemini-3.5-flash-lite`.



Because `ai.analyze_sentiment` expects a `REFCURSOR`, open a cursor for the single text column that you want to analyze. The function returns a result cursor containing `input` and `output` columns for each row.

The following example opens a cursor on the `review_content` column from the `reviews` table and passes it to `ai.analyze_sentiment`:
    
    
    -- Run the cursor logic in an anonymous PL/pgSQL block
    DO $$
    DECLARE
      prompt_cursor REFCURSOR;
      result_cursor REFCURSOR;
      rec RECORD;
    BEGIN
      -- 1. Open the input cursor
      OPEN prompt_cursor FOR
        SELECT review_content
        FROM reviews
        ORDER BY id;
    
      -- 2. Pass the input cursor to the function; it handles the processing and returns a result cursor
      result_cursor := ai.analyze_sentiment(
        input_cursor => prompt_cursor,
        batch_size => 10
      );
    
      -- 3. Loop through and print the results
      LOOP
        FETCH result_cursor INTO rec;
        EXIT WHEN NOT FOUND;
        RAISE NOTICE 'Review: %, Sentiment: %', rec.input, rec.output;
      END LOOP;
    
      -- 4. Clean up cursors
      CLOSE prompt_cursor;
      CLOSE result_cursor;
    END;
    $$;
    

The following is the example output:
    
    
    NOTICE:  Review: This movie is very good, Sentiment: positive
    NOTICE:  Review: The actors play the parts well, Sentiment: positive
    NOTICE:  Review: I like the music in this film, Sentiment: positive
    NOTICE:  Review: The story is easy to follow, Sentiment: positive
    NOTICE:  Review: Many people will enjoy this show, Sentiment: positive
    NOTICE:  Review: The film is too long, Sentiment: negative
    NOTICE:  Review: I do not like the ending, Sentiment: negative
    NOTICE:  Review: This movie is very boring, Sentiment: negative
    NOTICE:  Review: The story is okay, Sentiment: neutral
    NOTICE:  Review: Some parts are fine, Sentiment: neutral
    

## Limitations

Consider the following limitations when using the `ai.analyze_sentiment` function:

  * LLMs might occasionally generate unexpected output. If the model returns a value other than `positive`, `negative`, or `neutral`, then the `ai.analyze_sentiment` function returns `NULL` for that input instead of failing with a query error. The array-based version also returns a warning message and places `NULL` at that item's position in the output array.
  * The `ai.analyze_sentiment` function returns an error (`Invalid input: input cannot be null or empty.`) if the input text is `NULL`, an empty string (`''`), or contains only spaces, or if you pass a `NULL` or empty array to the array-based version.
  * Model latency affects query performance. The observed query latency is similar to the latency of a REST request made to the model.



## What's next

  * [Summarize content](https://docs.cloud.google.com/alloydb/docs/ai/summarize-content).
  * Read the [AI functions overview](https://docs.cloud.google.com/alloydb/docs/ai/ai-query-engine-landing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
