---
url: https://saif.google/secure-ai-framework/components/
title: Components of Generative AI Systems - SAIF
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:34:02.274951+00:00
---

# Components of Generative AI Systems - SAIF

> Source: https://saif.google/secure-ai-framework/components/

![](https://www.gstatic.com/marketing-cms/assets/images/72/20/a88c4007421393761c4797d2e1b5/map-icon.svg)

# SAIF risk map components

  
The SAIF mapping diagram categorizes AI development into four areas:   
  


  * Data
  * Infrastructure
  * Model
  * Application

  
This framing represents the broadened scope of AI development compared to traditional software development. In addition to the familiar code, infrastructure, and application components, AI introduces the complexities of data, training, and model development. Understanding how these dimensions work together is crucial to assessing the unique risks of AI development. The controls suggested to address the risks across this framing all align with the six core elements of SAIF. 

  * Data
  * Infrastructure
  * Model
  * Application



## Data components

Traditional software development follows predictable instructions: the user inputs trigger static code, which determines the logic driving outcomes of the program. In AI development, data takes on aspects of the role previously played by code—which transforms the security and privacy risks.

AI models are dynamic systems. They rely not only on their static code and user inputs, but also on learned patterns encoded in their internal parameters, referred to as 'model weights.' These weights are derived from the model's training data and training processes.

Compromising these model weights can have a significant impact on the model's behavior and outputs. This makes attacks on model weights as potentially damaging as attacks targeting the code in traditional software development.

There are three main data components in the SAIF Risk Map:

Expand all Collapse all

##  Data Sources

### Data Sources

The original sources or repositories from which data is gathered for potential use in training an AI model. These can include databases, APIs, web scraping, or even sensor data. The quality and diversity of data sources significantly impact the model's capabilities. 

The original sources or repositories from which data is gathered for potential use in training an AI model. These can include databases, APIs, web scraping, or even sensor data. The quality and diversity of data sources significantly impact the model's capabilities.

##  Data Filtering and Processing

### Data Filtering and Processing

The processes of cleaning, transforming, and preparing raw data from various sources to make it suitable for training. This may include labeling data, removing duplicates or errors, and even generating new synthetic data to enhance the model's learning. 

The processes of cleaning, transforming, and preparing raw data from various sources to make it suitable for training. This may include labeling data, removing duplicates or errors, and even generating new synthetic data to enhance the model's learning.

##  Training Data

### Training Data

The final, curated subset of data that is fed into the AI model during the training process. This data is used to adjust the model's internal parameters, enabling it to learn patterns and make predictions or inferences. 

The final, curated subset of data that is fed into the AI model during the training process. This data is used to adjust the model's internal parameters, enabling it to learn patterns and make predictions or inferences.

## Infrastructure components

The data components of AI development depend on the infrastructure underpinning with secure hardware, resilient code, data storage, and development and deployment platforms. Risks to this infrastructure can affect model and framework code, model and data storage, and model serving.

Attackers could try to poison, manipulate, or steal the data, models, or weights held in storage. If the model source code, dependencies, or any tools used to create and deploy them aren’t protected, attackers could tamper with them to create drastic changes to the model’s behavior, causing major security issues.

The first step in securing these infrastructure components is to apply traditional security practices to the physical environments used for training, storage and serving. Host and network security is needed to restrict potential attackers. Authentication and authorization for any access to the physical environments is essential. Software supply chain integrity for all traditional software dependencies should be considered.

Looking at the supplemental risks that are introduced by AI, infrastructure components in the SAIF Risk Map are:

Expand all Collapse all

##  Model Frameworks and Code

### Model Frameworks and Code

The code and frameworks necessary to train and use a model. Model code defines the model architecture and number and types of layers in the model. Framework code implements the steps for each layer to train and evaluate the model. The framework code is generally necessary not just for training a model, but also required to run inferences (i.e., make predictions) when the model is in use. Usually framework code is shipped separately from the model itself and needs to be installed to use the model. 

The code and frameworks necessary to train and use a model. Model code defines the model architecture and number and types of layers in the model. Framework code implements the steps for each layer to train and evaluate the model. The framework code is generally necessary not just for training a model, but also required to run inferences (i.e., make predictions) when the model is in use. Usually framework code is shipped separately from the model itself and needs to be installed to use the model.

##  Training, Tuning, and Evaluation

### Training, Tuning, and Evaluation

The process of teaching a model to extract the correct patterns and inferences from data by adjusting the probability of a given outcome (training), adjusting a smaller set of probabilities to tune a model to a specific task (tuning), and testing the model against new data to see how well it performs (evaluation). Given the enormous cost of training, many model creators take a preexisting model and tune it to their needs, by focusing only on the training related to a specific type of task. Evaluation happens in two stages: during the training process, when each checkpointed update to the model is evaluated, and after the model is trained, to assess how well it performs at its intended purpose. 

The process of teaching a model to extract the correct patterns and inferences from data by adjusting the probability of a given outcome (training), adjusting a smaller set of probabilities to tune a model to a specific task (tuning), and testing the model against new data to see how well it performs (evaluation). Given the enormous cost of training, many model creators take a preexisting model and tune it to their needs, by focusing only on the training related to a specific type of task. Evaluation happens in two stages: during the training process, when each checkpointed update to the model is evaluated, and after the model is trained, to assess how well it performs at its intended purpose.

##  Data and Model Storage

### Data and Model Storage

Storage for training data and (separately) the model. Training data is stored from ingestion through filtering and usage during training. Model storage refers to multiple stages in the development process:   
  


  * Local storage during training, in which each checkpoint is stored until overwritten;
  * Published storage, after training is completed and the model is uploaded to a model hub (a centralized model repository).

  
Note: Many model consumers use remote models served by API. Those model consumers that store models themselves, though, should consider the same Model Storage risks that apply to model creators. 

Storage for training data and (separately) the model. Training data is stored from ingestion through filtering and usage during training. Model storage refers to multiple stages in the development process:  
  


  * Local storage during training, in which each checkpoint is stored until overwritten;
  * Published storage, after training is completed and the model is uploaded to a model hub (a centralized model repository).

  
Note: Many model consumers use remote models served by API. Those model consumers that store models themselves, though, should consider the same Model Storage risks that apply to model creators. 

##  Model Serving

### Model Serving

The systems and process to deploy a model in production, making them available for services and applications.   
  
Note: Many model consumers use remote models served via API. Those that serve their own models, though, should consider the same Model Serving risks that apply to model creators. 

The systems and process to deploy a model in production, making them available for services and applications.  
  
Note: Many model consumers use remote models served via API. Those that serve their own models, though, should consider the same Model Serving risks that apply to model creators.

## Model components

The central concept for AI-powered applications is the model. The purpose of a model is to apply the statistical patterns extracted from training data and use these to generate new text, images, videos, or other output data (also known as inferences) from input data provided to it.

Model components in the SAIF Risk Map consist of:

Expand all Collapse all

##  The Model

### The Model

A pairing of code and weights, created with data during a training process. In the SAIF Risk Map, the model is represented as the result of the output of the Data Components being trained, stored, and served using the Infrastructure Components. A model is ultimately useful when deployed in applications, using Application Components. 

A pairing of code and weights, created with data during a training process. In the SAIF Risk Map, the model is represented as the result of the output of the Data Components being trained, stored, and served using the Infrastructure Components. A model is ultimately useful when deployed in applications, using Application Components.

##  Input Handling

### Input Handling

Input handling components filter, sanitize, and protect against potentially malicious inputs, whether from a user or more generally from anything outside the trusted system. Input handling acts as a control against numerous risks and is an area ripe for more research and development. 

Input handling components filter, sanitize, and protect against potentially malicious inputs, whether from a user or more generally from anything outside the trusted system. Input handling acts as a control against numerous risks and is an area ripe for more research and development.

##  Output Handling

### **Output Handling**

Similar to input handling, output handling components filter, sanitize, and protect against unwanted, unexpected or dangerous outputs from a model. Output handling is a major line of defense against various risks and an area primed for more development. 

Similar to input handling, output handling components filter, sanitize, and protect against unwanted, unexpected or dangerous outputs from a model. Output handling is a major line of defense against various risks and an area primed for more development.

## Application components

Users interact with AI models differently than with traditional algorithm-based searches and services. Some AI models act in response to more natural user prompting, with wording and phrasing choices directly affecting how an LLM, for example, infers requests, actions, and intent. When compared to interactions processed through an API, this more direct interaction introduces new avenues of risk, such as prompt injection.

Additionally, Generative AI models are increasingly used as agents or assistants that can act on a user’s behalf to provide helpful functions. In these situations, AI models are interacting with other systems to get information or run specialized computational functions, including state-changing actions. While this networking opens up exciting possibilities of more complex behaviors, each connection also increases the potential impact of a successful attack on the AI model or network.

Application components in the SAIF Risk Map are:

Expand all Collapse all

##  Application

### Application

The application, product, or feature that uses an AI model for functionality. These applications might be directly user-facing, as in the case of a customer service chatbot, or the “user” might be a service within an organization, querying the model to power an upstream process. If an application has the ability to execute tools on behalf of its user, it is sometimes referred to as an Agent. 

The application, product, or feature that uses an AI model for functionality. These applications might be directly user-facing, as in the case of a customer service chatbot, or the “user” might be a service within an organization, querying the model to power an upstream process. If an application has the ability to execute tools on behalf of its user, it is sometimes referred to as an Agent.

##  Agent

### Agent

A service, application, or additional model called by an AI application or model to complete a specific task (also known as “tool use”). Since agents/plugins may call on external data or trigger requests to another model, each use of a plugin may open a transitive set of risks, multiplying the risks already present in the AI development process. 

A service, application, or additional model called by an AI application or model to complete a specific task (also known as “tool use”). Since agents/plugins may call on external data or trigger requests to another model, each use of a plugin may open a transitive set of risks, multiplying the risks already present in the AI development process.

  * ![](https://www.gstatic.com/marketing-cms/assets/images/e9/bc/394093d7467588f812f19c1b266d/g-shield-lockup-footer.svg)



