---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/
title: Incrementing a Firestore document field while using shards \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:15:25.371663+00:00
---

# Incrementing a Firestore document field while using shards  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/

[ Skip to main content ](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/)
  * [Deutsch](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=de)
  * [Español](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=it)
  * [Português](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffirestore%2Fdocs%2Fsamples%2Ffirestore-solution-sharded-counter-increment%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/docs)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)


Was this helpful?
#  Incrementing a Firestore document field while using shards Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#whats-next)


Incrementing a Firestore document field while using shards
## Explore further
For detailed documentation that includes this code sample, see the following: 
  * [Support frequent and distributed counters](https://docs.cloud.google.com/firestore/native/docs/solutions/counters)


## Code sample
[C#](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#c)[Go](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#go)[PHP](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#php)[Python](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#python)[Ruby](https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/#ruby) More
To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
/// <summary>
/// Increment a randomly picked shard by 1.
/// </summary>
/// <param name="docRef">The document reference <see cref="DocumentReference"/></param>
/// <returns>The <see cref="Task"/></returns>
private static async Task IncrementCounterAsync(DocumentReference docRef, int numOfShards)
{
    int documentId;
    lock (s_randLock)
    {
        documentId = s_rand.Next(numOfShards);
    }
    var shardRef = docRef.Collection("shards").Document(documentId.ToString());
    await shardRef.UpdateAsync("count", FieldValue.Increment(1));
}
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```

// incrementCounter increments a randomly picked shard.
func (c *Counter) incrementCounter(ctx context.Context, docRef *firestore.DocumentRef) (*firestore.WriteResult, error) {
	docID := strconv.Itoa(rand.Intn(c.numShards))

	shardRef := docRef.Collection("shards").Doc(docID)
	return shardRef.Update(ctx, []firestore.Update{
		{Path: "Count", Value: firestore.Increment(1)},
	})
}

```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
$ref = $db->collection('samples/php/distributedCounters');
$numShards = 0;
$docCollection = $ref->documents();
foreach ($docCollection as $doc) {
    $numShards++;
}
$shardIdx = random_int(0, max(1, $numShards) - 1);
$doc = $ref->document((string) $shardIdx);
$doc->update([
    ['path' => 'Cnt', 'value' => FieldValue::increment(1)]
]);
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
def increment_counter(self, doc_ref):
    """Increment a randomly picked shard."""
    doc_id = random.randint(0, self._num_shards - 1)

    shard_ref = doc_ref.collection("shards").document(str(doc_id))
    return shard_ref.update({"count": firestore.Increment(1)})

```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
# project_id = "Your Google Cloud Project ID"
# num_shards = "Number of shards for distributed counter"
# collection_path = "shards"

require "google/cloud/firestore"

firestore = Google::Cloud::[Firestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html) project_id: project_id

# Select a shard of the counter at random
shard_id = rand 0...num_shards
shard_ref = firestore.doc "#{collection_path}/#{shard_id}"

# increment counter
shard_ref.update({ count: firestore.[field_increment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client.html)(1) })

puts "Counter incremented."
```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
