---
url: https://saif.google/ai-development-primer/
title: Secure AI Development Primer: Build Secure AI Systems - SAIF
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:34:12.957791+00:00
---

# Secure AI Development Primer: Build Secure AI Systems - SAIF

> Source: https://saif.google/ai-development-primer/

![](https://www.gstatic.com/marketing-cms/assets/images/97/2b/75084f9e41a3a1878fe5dbc55580/ai-development-primer-icon.svg)

# Secure AI Development Primer

  
This primer provides an introduction to the AI development lifecycle, specifically highlighting the security and data protection risks that can emerge at each stage. It is intended for both security practitioners and AI developers. 

  * Introduction
  * Data
  * Infrastructure
  * Application



## Introduction

Security practitioners need a deep understanding of the systems they are protecting, but many aspects of these systems are not yet widely understood to those outside AI development roles. After reading this Primer, a security practitioner will understand how data, infrastructure, and applications fit together with AI models and will understand the origins and causes of the many risks they need to protect against.

AI developers, on the other hand, will understand the impact on security from the various choices they make during the development process. With awareness of the security implications, they’ll be able to choose more secure options. A holistic understanding of how risks accumulate throughout the development process—and how seemingly isolated decisions can have far-reaching consequences—is crucial for building secure and robust AI systems.

This primer assumes that an organization has already identified a business case for the use of generative AI and has clearly defined the problem its use will solve, in order to guide model selection and development decisions. Assuming those important first steps, the primer begins by exploring the curation and creation of a model from data, showing its foundational role in the development process and the security implications of choosing and processing data. Next is a discussion of the infrastructure (systems, code, storage, and serving) required to support the AI development process. Finally, there is an examination of considerations specific to the development of applications that use these models.

Although not covered in a single dedicated section, the model itself remains a central character throughout this narrative. While the primary focus is Generative AI—models that create new content from existing data—the overarching principles and risks discussed here apply similarly to various AI models, regardless of format, size, or purpose.

## Data

The creation of any AI model requires data for training. Data is just as important as model architecture source code: even the most complex model can only perform well when trained on suitable data. Moreover, given the possibility of a model memorizing and reciting from training data, models can effectively inherit risks within that data.

Expand all Collapse all

##  Data sourcing and ingestion

### Data sourcing and ingestion

Therefore, **data sourcing** requires careful consideration from the outset. Developers can ask themselves key questions early on, each of which can affect the built-in security and data governance features of the model.

  * What is the intended use case for the system, and what questions need to be answered to accomplish this task?
  * What data could train the model to answer these questions?
  * What data sources align with the needs of both practitioners and end users?
  * Is the data high-quality, complete, accurate, and relevant?
  * Is there a way to verify that the data sources haven’t been compromised or manipulated, such as cryptographic signatures that reveal tampering? 
  * What are the relevant rights to use the data, and how are those rights documented and tracked?
  * Are there any ethical concerns or potential biases associated with the datasets? 
  * Are there any legal issues or risks to business associated with the datasets, and what oversight can ensure the legality of data before launch?



“Using unauthorized training data can cause long-lasting risks.”

Data sourcing and ingestion risks: unauthorized training data, data poisoning.

The first several points in the preceding list will be relevant to model performance, meaning both efficiency and behavior (discussed later in the paper). The latter points in the list are particularly relevant to risk management. Beyond assessing the data’s suitability and performance potential, developers should determine whether using it for training is even permissible, since using unauthorized training data can cause long-lasting risks.

For example, using copyrighted material could result in legal repercussions, and training on user data without proper consent might trigger policy or regulatory violations, potentially causing severe reputational or financial damage and requiring the model to be retrained or even retired from use. Practitioners may also consider perception and expectations around data use. For example, if a dataset contains information about people, are they aware their data could be used in this way?

Once suitable data sources have been identified and the data acquired, they’re typically ingested into local storage for faster training. This introduces another risk: the data could be maliciously poisoned before, during, or after ingestion into the organization’s systems. Data poisoning involves manipulating training data to alter the behavior of the models trained with that data. This manipulation can be direct or indirect, depending on whether it targets the datasets themselves or the data sources before they are ingested.

**Direct data poisoning** involves modifying existing data points or inserting malicious samples directly into the training dataset. For example, an insider tasked with manually labeling images for an abuse detection model might intentionally or unintentionally mislabel some examples, changing the model’s ability to classify certain types of abuse.

**Indirect data poisoning** , on the other hand, involves contaminating the data sources used to create the datasets. Attackers might pollute public information on the open web before it’s incorporated into datasets. This contamination might be overt, such as posting misinformation on social media sites, or it may be hidden within webpage text. It’s already been shown that [_misinformation information in a public help article_](https://www.ifixit.com/Guide/Data+Connector++Replacement/147712) can be [_surfaced by an LLM that ingests the information_](https://chatgpt.com/share/e52dc4dd-77e6-48a5-a7ca-77e3dfa39eb5).

##  Data cleaning and augmentation

### Data cleaning and augmentation

After ingestion, data typically requires transformation before it’s suitable for model training. This process, called **data cleaning** , addresses issues like missing values, duplicates, incorrect labels, dataset corruption, and sensitive data. Data cleaning may be performed manually through human inspection or at scale via automation.

Missing values might cause the model to fail to train due to numerical errors. Data duplication can bias the model, and incorrect labels could cause the model to learn unintended patterns. Dataset corruption can cause the training process to crash (if an error in reading data is not handled) or make the model learn incorrect patterns.

For the issue of sensitive data, developers can use data sanitization practices that reduce the impact of data disclosure. For instance, practitioners could remove identifiers from the training set to reduce potential harms that could emerge if data were disclosed. Different sanitization practices may be appropriate for different datasets. For example, when training on public data, it may be desirable to retain individuals’ names, so the model can respond to queries about public individuals; yet, numbers that appear to be credit card information might be filtered regardless of data source.

Practitioners can also investigate which data cleaning and sanitization practices work for the specific modalities of data they are training on. For example, removal of some types of identifying information from visual data can be done in an automated fashion, such as blurring faces. However, removing contextual visual information (such as identifying and blurring an accidentally captured identity document) is more difficult than removing the same information from textual data.

Sometimes, practitioners combine multiple data sources to enhance model training. This isn’t as simple as merely merging the data, since the various sources might use different schemata. Practitioners would need to transform data from one format to another or convert from one unit of measurement to another (from Celsius to Fahrenheit in weather data, for example).

Finally, to generate more data for training and highlight relevant features, practitioners may create synthetic data that’s artificially manufactured. This can be done using another model or through deterministic data manipulations, such as rotating or mirroring images of objects.

“Each of the stages of data cleaning and transformation introduces the potential of data poisoning or other types of tampering.”

Collectively, all these processes that manipulate data formats to make it more suitable for the training pipeline are known as **data augmentation**. The quality of these transformations significantly impact the trained model’s performance.

Since these transformations result in datasets that are different from their original form, it’s important from a data integrity perspective to keep records of these operations. This concept is known as **lineage** : capturing metadata about datasets, transformations, and the resulting models. Lineage resembles [_provenance_](https://slsa.dev/spec/v1.0/provenance) in the traditional software supply chain, though provenance is broader, encompassing infrastructure metadata and cryptographic signatures for inputs and outputs.

Ideally, a developer would capture both lineage and provenance for datasets and processes performed on them. For complete lineage, the original sources of data (see “Data sourcing and ingestion”) should also be included in the corresponding provenance document, and recorded during the data sourcing phase to ensure complete lineage.

Data cleaning and augmentation risks: data poisoning, excessive data retention, sensitive data disclosure

First, if sensitive data isn’t sanitized during these steps, it’s possible the model could disclose it later during usage, introducing data management and privacy risks.

Furthermore, each stage of data cleaning and augmentation introduces the potential of data poisoning or other types of tampering. Given the critical role of training data in a model’s post-training performance, capturing comprehensive lineage and provenance information is essential.

For example, human intervention during any of these stages introduces the risk of malicious or accidental mislabeling, while automated processes using an algorithmic labeler can suffer from bugs that lead to improper data transformations. Both scenarios can impact the trained model’s performance, effectively becoming a form of data poisoning—a serious risk during data ingestion, cleaning, and augmentation.

“Lineage and provenance contribute to data management and model integrity, and forms the foundation for AI model governance.”

Lineage and provenance contribute to data management and model integrity, and forms the foundation for AI model governance, including supporting policies and controls for the use of copyrighted materials in training. Lineage and provenance also support management of data that has a limited allowed retention period, supporting the data governance needed to protect against the risk of excessive data retention.

##  Training

### Training

The next development step is using the datasets to create a model. At a very high level, a model is a collection of weights—parameters that determine how each feature (data attribute, data column, etc.) influences the output. These weights are established through a process known as **training,** where they are adjusted until the model’s predictions closely match the desired outcomes. (For an introductory explanation of the process, see this [_Machine Learning crash course_](https://developers.google.com/machine-learning/crash-course/descending-into-ml/linear-regression).)

As a light-hearted example, imagine selecting daily lunches for a picky eater. You’d consider various factors: recent meals, food temperature, flavor profiles, color, texture, nutritional value, season, and even dining companions. Some factors would play a larger role than others, and their importance (**weight**) might depend on the other factors’ values. By tracking the picky eater’s preferences and mapping them to these factors (or **features**), you can gradually learn their relative weights, inferring a decision tree that helps you plan better menus.

For small models, training often starts from scratch with random weights values. The trainer traverses the training data multiple times and iteratively adjusts the values, updating the weights so that the prediction errors (**loss values**) become lower. Practitioners usually monitor loss plots and other metrics to evaluate the training progress, allowing them to stop the training early if a model isn’t suitable or it learned exceptionally fast.

However, as the model complexity increases—as with [_large language models (LLMs)_](https://developers.google.com/machine-learning/resources/intro-llms) and multi-modal [_foundation models_](https://research.ibm.com/blog/what-are-foundation-models) that are trained to perform a large variety of tasks—training from scratch becomes less common due to the computational demands. The same concepts of features, target labels, and loss apply, but now the training process is broken up into multiple runs. Between each run, practitioners inspect the resulting model, analyze its performance on new datasets used for evaluation, and select new sources of data for the next training run.

Since training large models from scratch is expensive, taking massive amounts of time and resources, developers frequently start with a pretrained model and construct a new model on top. One method is****[**_transfer learning_**](https://www.tensorflow.org/tutorials/images/transfer_learning), which teaches a model trained for a specific task to perform a different task. **Finetuning** is a type of transfer learning that freezes most of the model weights and updates only the last few computations in the model architecture.

These techniques allow models to be taught new tasks with less effort and cost than training from scratch. For example, a model trained on a large, general-purpose image recognition dataset can be specialized for X-ray diagnostic tasks using a smaller dataset of medical scans.

Training risks: model source tampering

Training and fine tuning subject a model to supply chain security threats. It’s important to record the provenance and lineage for every training dataset, metadata from any training processes, and the provenance of the pretrained model itself. A poorly protected or untraceable generic model could pose a risk for any models derived from it, since it could have been maliciously trained with backdoors or to perform poorly on certain tasks. Additionally, it could have been tampered with between training and finetuning. Provenance also helps if the training environment is discovered to have been compromised, allowing identification of models that may have been affected.

##  Evaluation

### Evaluation

When training models, we want to make sure they perform effectively at their task without **overfitting** for that task, which is when a model performs exceptionally well on training data but fails to perform given new data. Overfitting is comparable to a model memorizing training data, but not being able to generalize to new situations.

Evaluation to address overfitting can happen at multiple points:

  * **Automated testing during training:** The data is randomly split into training and test sets. The training data is used to adjust the model weights, while the test data is used periodically during training to evaluate the model performance on unseen examples. 
  * **Human evaluation between training runs:** LLMs and foundation models are also evaluated by humans using reinforcement learning with human feedback (RLHF). Periodically, humans rate model responses to various prompts, creating a new dataset to improve future training rounds.



Larger models, such as LLMs and foundational models, are also [_evaluated after release_](https://github.com/openai/evals), often by third parties. These evaluations are similar to integration tests or acceptance testing in traditional software, allowing organizations to assess model performance before deployment. Organizations prioritizing production hygiene and observability might conduct these tests in trusted execution environments and record the results in a signed attestation, so that they can ensure and provably demonstrate that models have been adequately evaluated before use.

Practitioners can also evaluate the model for privacy measures. For instance, they can measure memorization (i.e., how much the model is recalling specific data from training and prompts). The potential impact of memorization can be reduced with techniques such as generalizing data, so that the memorized data would be less specific—and potentially harmful—if disclosed.

Evaluation risks: data poisoning

RLHF and related techniques influence the resulting model, so provenance for these processes must be recorded in the model’s supply chain metadata. RLHF is vulnerable to data poisoning: someone could pollute the user feedback loop by maliciously encouraging incorrect answers. Recording provenance allows organizations to trace the impact of such manipulations once they are discovered.

## Infrastructure

The AI development process relies on secure infrastructure, particularly for model training, as well as storing, executing, and serving code for both models and data. Though not discussed, traditional security practices are also assumed. For example, access control, network security, traditional software supply chain integrity and vulnerability management are all essential to secure development, whether or not AI is involved.

Traditionally, model frameworks and code might be considered part of a secure development life cycle (SDLC), more related to software than infrastructure. Given the fundamental role of model and framework code in training models, we consider this code (and the training processes associated with them) to be part of the infrastructure that supports model development.

Expand all Collapse all

##  Model and framework code

### Model and framework code

AI practitioners rarely write code from scratch to train models. Instead, they use ML libraries like JAX, TensorFlow, or PyTorch, which leverage hardware accelerators (GPUs and TPUs) for faster training. For large models, the training framework can distribute computation across multiple hosts, managing scheduling and network communication optimally. The framework is necessary for model training, model evaluation, and using the model at inference. Since it needs to be available throughout the lifecycle, the framework is essentially a build-time dependency when the model is trained and a run-time dependency when the model is used in applications for inference.

“The framework and training libraries are a critical part of the supply chain, since their vulnerabilities can affect the resulting models.”

The ML frameworks are packages built from source code (the **framework code**), so these might be impacted by vulnerabilities or compromised through traditional software supply chain attacks. The framework and training libraries are therefore a critical part of the supply chain, since their vulnerabilities can affect the resulting models. Recording provenance for ML frameworks allows us to identify models trained with frameworks later found to have a vulnerability.

**Model code** , which is separate from the framework code, defines the model’s architecture using the ML frameworks’s API. This code is translated into a **computation graph** , recording all the computations during training and inference. Popular ML frameworks simplify development by using **layers** : collections of computational units that perform similar tasks. For example, a convolutional layer is used in image processing to perform a computation for each pixel, based on the value of the pixel and its neighbors—a learnable version of [_filters_](https://ai.stanford.edu/~syyeung/cvweb/tutorial1.html) used in non-AI-based image processing.

The model code defines how many of these layers and types of layers make up the model. Depending on the model serialization format, practitioners either need to copy the code to make it available at inference time or serialize the code inside the model format. In the latter case, the ML framework also contains code to be able to interpret the model code, much like Java’s runtime environment (JRE) interprets Java bytecode.

Model and framework code risks: model source tampering

The model source code is important, as it dictates all the computations the model performs. A malicious actor could add layers that consume time without producing useful results. Given the power of modern ML frameworks to handle many training and inference scenarios, dangerous operations can also appear in a model’s computation graph. For example, distributed training requires operations that send or receive data over networks. Attackers could combine these with file read/write operations to exfiltrate data from training systems, including credentials to data or model storage, training data, or even other files in the filesystem.

Similarly, an attacker could exploit vulnerabilities in the framework by manipulating the interaction between the model code and framework code. For example, a vulnerability in the framework’s image parsing code could allow attackers to execute arbitrary code on servers using the model. The complexity of the interplay between the framework code and the model code means there are many opportunities for vulnerabilities to be introduced.

The robustness of the code is another concern. Some model frameworks allow powerful computations, potentially enabling insertion of backdoors into the model. For example, if the model code uses layers for certain computations (e.g., [_the Lambda layers in TensorFlow/Keras_](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda)), one of these layers could be altered to perform malicious actions. If the affected computation is essential for the model's behavior, removing the backdoor might require entirely retraining the model, a costly and labor-intensive process.

“The code might allow excessive access to data, allowing for silent data poisoning during training—a security risk that’s exceedingly difficult to detect.”

Finally, the code might allow excessive access to data, allowing for silent data poisoning during training—a security risk that’s exceedingly difficult to detect. Attackers might even exploit model vulnerabilities to write to the data storage layer that stores data for training other models in the future. Consequently, it’s essential to have infrastructure safeguards in place to ensure that a training job has access only to the data it needs during training.

##  Data storage

### Data storage

The need for infrastructure safeguards highlights another important topic: storage. Different developers need to store and access data, code, and models at different times and places. Code storage is a topic best addressed through standard software development practices. The storage of data and model weights, though, have challenges specific to ML development.

Data requires storage throughout ingestion, cleaning, augmentation, training, and evaluation. Due to the data-intensive nature of AI development, data storage is an important security concern. Protecting training data from tampering and unauthorized access while in storage is necessary to protect against potential manipulations of the models trained on that data.

During initial data curation, raw data may come in multiple formats (text, images, audio, video, sensor readings) in massive volumes. This poses security challenges for storage. Large datasets may require distributed storage systems, such as GCP Cloud Storage buckets, AWS S3 buckets, or dedicated storage provided by popular model and data repositories (e.g., [_Kaggle_](https://www.kaggle.com/datasets), [_Hugging Face_](https://huggingface.co/datasets)).

Data storage risks: data poisoning

If not properly configured and protected with robust access controls, encryption, and integrity checks, the data could be tampered with. A credential leakage allowing unauthorized data modification could lead to direct data poisoning, impacting all models trained from this data. These integrity concerns also extend to data cleaning and augmentation processes.

During training and tuning, there is an additional concern of proximity. To optimize efficiency, datasets need to be stored near the compute resources used to update the model weights while training, minimizing latency from reading vast amounts of data across large clusters of compute. This adds to the complexity of data movement and protection during training.

##  Model storage

### Model storage

For models, storage affects:

  * Framework code: stored in source control, with released versions of the frameworks kept on the ecosystem’s package repository (e.g. PyPI for Python packages).
  * Model code: stored in source control, at least during training. Depending on the model delivery method, this code might also need to be distributed with the application. 
  * Model weights: stored during training (as **checkpoints** from which training can be resumed) and post-training, including during model deployment.



Model weights need protection throughout training and storage, while being transferred through several formats. For example, the training process updates the model weights to refine model performance, minimizing its errors at the assigned task. To use the model, those weights must be transferred to the application. This involves **serializing** the model—recording the weights in a standardized file format that the application can interpret.

Training runs are lengthy and resource-intensive, so hardware failures may require restarting the process. To avoid starting over, saved checkpoints are used. Most training processes save checkpoints periodically (e.g., after each complete traversal of the data). For efficiency, checkpoints typically save only the numerical weights without any additional metadata, since only the numerical weights are updated between checkpoints.

Large models may use checkpoints for techniques like RLHF or to initiate a new training run on a new dataset. Generally, these checkpoints are only temporary, retaining only the most recent model state. At the end of the training runs, practitioners usually select one checkpoint (usually the latest, but sometimes earlier ones with better performance metrics) and move it to a model hub, potentially in a different format. From the model hub, the weights can be downloaded for use in applications.

When transferring models, a more detailed serialization format is needed than when checkpointing due to differences between training and production infrastructure. This involves bundling weights and model architecture into a single package. A model interpreter (provided by the ML framework) is integrated within an application to parse the structure and weights, constructing the appropriate memory layout for inference. This means the framework needs to be a run-time dependency of the application.  
A single package also allows the interpreter and the framework used to train the model to evolve independently. As long as compatibility is maintained, models trained with one version of the framework can be used with an interpreter matching another version. For some of the existing serialization formats, it’s possible to achieve both forward and backward compatibility, achieving a full decoupling between the training process and the applications that use the models in production. This decouples training from production, unlike using just checkpoints alone, where model code must be unchanged and architecture changes necessitate retraining.

Model storage risks: model source tampering

All forms of storage may pose security risks (see [_Securing the AI Software Supply Chain_](https://research.google/pubs/securing-the-ai-software-supply-chain/) for more discussion). Overall, we need to remember that _models are not easily inspectable_ : their behavior depends on a vast number of weights, impossible to manually analyze because of the sheer number and binary formats. Some storage formats even make it difficult to analyze the computational graph. It’s better to treat models as programs, similar to bytecode interpreted at runtime. Any change can have significant, unpredictable impacts downstream, unlike traditional binary software which might be understood via reverse engineering.

Since models are costly and complex to build, we should ensure the integrity of every intermediate artifact and track all inputs. This is achieved by maintaining a complete supply chain provenance.

As an example of provenance’s usefulness, consider an attack on the training platform that introduces a backdoor into all models trained there (similar to a scenario [_where converting models to SafeTensors generated corrupted models_](https://hiddenlayer.com/research/silent-sabotage/) because one model was able to infect the entire environment). Provenance can help identify which models have been compromised once the attack is discovered.

Finally, verifying provenance ensures that the deployed models are the expected ones. Just as with traditional software, every dependency must come from trusted sources, or else unwanted behavior can occur. For example, deploying an LLM for a help chat application without verifying its provenance could result in the chatbot outputting offensive text to the users, losing user trust.

##  Model serving

### Model serving

After training finishes, the model is ready for use in a production pipeline. **Model serving** is the process of making a model’s inferences available to applications or products.

There are two primary serving methods:

**Remote-API gated models** : the model resides on a server, accessed via API or dedicated service. This is common for large models, offering benefits like easy updates to the model without changing the application. There’s also centralized management for monitoring, maintenance, and scaling. Access controls and rate limiting can prevent abuse, while filtering can mitigate unwanted behaviors or temporarily fix model errors.

**Packaged models** : The model is directly integrated into an application, product, or device itself, This is more common with smaller models and applications that need to run offline or have strict latency requirements.

Model serving risks: model exfiltration, model deployment tampering

For remote API-gated models, there is a risk of attackers making excessive calls to the API in order to reverse engineer the model’s weights based on the responses. Rate limiting and authentication are necessary to limit the calls, and therefore data about the model that an attacker can receive.

For packaged models, model exfiltration is also a persistent risk if an attacker can access the model files. Encryption of the model and weights at rest can help.

Regardless of the method, model deployment tampering is a risk during model serving. Attackers may modify or swap the model file during deployment. The mitigations using model integrity, provenance and signatures, and verification discussed earlier are necessary to prevent this potentially devastating type of attack.

As mentioned in the Model Frameworks and Code section, model inference requires installation of the model framework. These frameworks are not shipped with the models; instead, the application creator has to download it from the package manager. If the package isn’t protected against supply chain attacks with traditional secure software practices, the framework can itself introduce the risk of model source tampering (if a tampered or insecure version is installed).

## Application

Finally, the model is ready to be put to use in an application. In many ways, the AI application development process is similar to traditional application development. Differences arise, though, where the application relies on a model instead of code to drive actions.

There are several key stages of application development to consider for security risks: model selection, user interactions, agent and tool usage, and model integration. The section ends with a brief discussion of application testing, to detect risks across the development lifecycle.

Expand all Collapse all

##  Model selection

### Model selection

Even within the same organization, application creation and model training are typically handled by different teams. Application creators may choose to access a model provided through an API service, purchase a model, or download a model from a freely available model hub such as Kaggle or Hugging Face. From the application creator’s perspective, **model selection** is one of the most important choices they can make, as it directly impacts the quality and security of their application.

When choosing a model, an application creator should consider:

  * **Purpose** : does the model’s intended application or specialization align with the application’s goals?
  * **Input types** : what inputs will the model process?
  * **Data quality and suitability** : was the model trained on relevant, high-quality data?
  * **Accuracy and performance** : how well did the model perform in testing?
  * **Tested usage scenarios** : was the model rigorously tested for the intended use case?
  * **Provenance and lineage** : does the model come with provenance and a model card to capture data about its lineage, testing, use cases, or other relevant information?



Model selection risks: model evasion, unauthorized training data, supply chain attacks, and insecure model output

When models are used in situations that they’re not intended or been adequately tested for, it’s more likely that a malicious attacker can manipulate and slightly alter inputs to confuse the model and change its inference. This attack is known as **model evasion**. For example, a model that is trained to recognize stop signs may produce the wrong inference if someone has applied stickers to the sign, obscuring the visual signals the model needs to correctly identify the sign. In this situation, knowing the quality of data, degree of testing, and performance accuracy for a model can help determine whether it is robust enough for a given task. Ideally, information about testing and usage scenarios can be captured in a model card that is circulated with the model.

Another model selection concern is related to unauthorized data usage: the application creator must be sure they are not selecting a model that was trained on data with incompatible use restrictions. For example, developers creating commercial applications should be aware of whether they’re considering using models trained on data that may not be monetized. Models trained or fine tuned on enterprise data for one customer should remain exclusive to that customer, and personalized models should not be repurposed. Application creators must consider all aspects of whether a model is fit for the intended use case before integrating it into their application.

AI applications often need to process various input formats like images, audio, and video alongside text. Both traditional and AI applications rely on third-party libraries for processing input, which could introduce vulnerabilities. AI models also introduce new concerns. For example, multimodal models can map different input types to various outputs (e.g., image-to-text, text-to-image). Applications must support this processing holistically.

One risk of multimodality is a failure to properly handle the various formats, leading to unexpected application behaviors. Attackers might attempt to bypass filters intended to block offensive inputs by encoding their prompts in different alphabets, or might try to evade output filtering by requesting outputs in specific languages or formats, such as poetry.

In addition, the increased dependencies from the libraries for each format—or the libraries offered to update those libraries—expand the transitive network of risks posed by a larger supply chain.

##  User interactions

### User interactions

User interactions introduce additional security and privacy considerations for AI application development. It’s important to be clear with users how their prompts or inputs to a model will be handled not only to build trust, but also to set clear expectations so a user can make educated decisions about using a model. If user inputs are used, it’s important to protect that data during later AI development.

Beyond this disclosure within the application interface, developers may choose to use input and output filtering for content sent to and from the model. These processes are in some cases provided by an API-based model service, or might be built within the application. Filtering can help partially mitigate multiple user-facing risks involving sensitive data, insecure model output, and prompt injection.

User interactions risks: prompt injection, inferred sensitive data, and insecure model output

One of the most discussed AI risks is prompt injection: when malicious users exploit the ambiguity between “instructions” and “input data” in a prompt to cause the model to do something it shouldn’t, similar to SQL injections in web applications and databases. Attackers can embed instructions as part of data, causing the LLM to leak sensitive information from the system of training set or otherwise misbehave. Commonly, the injection is used to bypass restrictions on what the model can output.

“Jailbreaks are a well-known type of prompt injection that tricks the model to ignore its safety training. Even with the best training, models are also at risk of “social engineering” through a jailbreak prompt.”

[_Jailbreaks_](https://arxiv.org/pdf/2307.02483.pdf) are a well-known type of prompt injection that tricks the model to ignore its safety training. These are the well-known "ignore your previous instructions" or “Do Anything Now” (DAN) attacks, which can cause a model to output unsafe content or leak personally identifiable information. Since the input is coming from an external user, the risk can be severe. Even humans cannot be trained to always resist social engineering; even with the best training, models are also at risk of “social engineering” through a jailbreak prompt.

Other information beyond user prompts may become confused in the integration of inputs and outputs, potentially leading to sensitive data disclosure. This includes data used for training, tuning, or prompt preambles (the prompt context that is not shown to the user but used to control the LLM). Several situations are of concern:

  * **Memorization** : the model reproduces portions of sensitive training data, like social media posts or proprietary code snippets, as part of the output. Recitation checkers that scan for verbatim repetition of training data [_may be insufficient_](https://arxiv.org/abs/2210.17546) and may not support all output modalities from a multimodal model. 
  * **Extraction** : attackers extract portions of the training data set, for instance by causing the model to nearly exactly reproduce images it was trained on, leading to privacy, data governance, or ethical concerns.
  * **Prompt inference** : confidential information included in the prompt preamble, which guides the model’s behavior, is leaked. This can include proprietary information or carefully engineered instructions.
  * [**_Membership inference attacks_**](https://arxiv.org/pdf/1610.05820.pdf): attackers infer whether a specific user or data point was used in the model’s training, which can reveal sensitive information, such as medical diagnoses.



Conversely, a related but distinct situation occurs when the model infers information about a user based on interactions, even if the information is not directly entered as a prompt. (Contrast this to membership inference attacks, where the user infers the information from the model, rather than the model from the user.) For example, a model might infer the political party of a user based on a query that includes their location.

This risk of **inferred sensitive data** is concerning for several reasons. First, if the information is accurate, users may perceive the situation as a privacy violation. Second, users could [_intentionally or unintentionally cause a model to infer sensitive information_](https://arxiv.org/pdf/2112.04359.pdf) about others.

At this stage, **insecure model output** is also a concern if the model’s output isn't properly sanitized and validated before being returned to the user (or an agent, as in the case of triggering a rogue action, discussed in the next section).

##  Agent and tool usage

### Agent and tool usage

AI applications are increasingly automating tasks for greater efficiency. For example, a model may plan and trigger a multi-step process such as reading an email, summarizing it, and composing a reply with a suggested meeting time. In these cases, the application is acting as an assistant or **agent**. To accomplish this, the model needs access to email and calendar services, which are **agents** —services, applications, or even other models that extend the capabilities of the AI application.

While this networking offers opportunities for more complex behaviors, it also amplifies security risks. Each connection to another agent increases the potential impact of vulnerabilities within the model or network, creating new entry points for malicious attackers. Furthermore, plugins may call on external data sources, introducing further risks. Since agents can be other AI models, the entire risk landscape is replicated for each added agent.

Agent and tool risks: rogue actions

One new risk is the potential for insecure model output to trigger **rogue actions** —when an AI output triggers unintended actions in other applications or models. Accidental rogue actions can occur when AI agents, acting on behalf of users, make errors in how they perceive information, reason about it, or plan the needed actions, potentially leading to significant changes in a system’s state.

“Accidental rogue actions can occur when AI agents, acting on behalf of users, make errors in how they perceive information, reason about it, and plan the needed actions.”

For example, an agent may read an email and set a new calendar appointment complete with driving directions that launch in a map application, but an error during reasoning could send the user to the wrong address. Likewise, a smart thermostat might track a resident’s daily routine and adjust the temperature accordingly, but an error in perception might result in overheating the home when no one is there. Given the unpredictable nature of LLMs, it’s crucial for application creators to carefully consider the potential impact of allowing AI agents to initiate powerful actions.

Malicious rogue actions, on the other hand, can result from users crafting inputs to manipulate the model output (such as prompt injection attacks). Since LLMs may produce answers that correspond to the beliefs of user prompts, an LLM can be “tricked” into triggering malicious actions that cascade through networked systems.

One approach to solving these challenges is to use **retrieval augmented generation** , or **RAG**. RAG pairs an LLM with an authoritative knowledge base, such as a collection of documents that is relevant for the application. When responding to a prompt, the system first searches the knowledge base for relevant information to inform the response.

For example, an LLM that answers questions about a company’s internal documentation would search those documents as its knowledge base, ensuring that the answers are grounded in relevant information rather than generic responses. RAG is useful for AI agents, since each agent can have its own specialized knowledge base to enhance decision-making.

##  Model integration

### Model integration

At this point, the model needs to be integrated with the application, either by being called through an API or packaged directly with the application. The various methods of model serving were discussed in an earlier section on Model Serving.

A consideration during integration is updates: AI models need frequent updates to stay effective, and AI applications need different update strategies than traditional software. Model upgrades may be more frequent due to changes in the data they encounter or new vulnerabilities. AI applications can be designed to allow upgrading just the model, separate from the code.

Complex model changes, like addressing security issues, take longer and might require gathering new data and retraining, taking weeks or months depending on the size of the model and the magnitude of the change. Developers may apply temporary fixes during this time by intercepting model inputs and outputs, such as outputting a standard message to the user (e.g., “Currently, this action is not supported”) in response to problematic classes of queries.

Updates may also be required due to **model drift** , when model inference abilities degrade due to changes in the environment. Models trained on current events or slang become outdated, and spam filters need updates as user language evolves. Regular updates and retraining with new datasets and classifiers are necessary. To simplify the manual process of keeping model dependencies up to date, [_Kaggle_](https://www.kaggle.com/) and [_Hugging Face_](https://huggingface.co/) currently offer libraries for framework dependency management.

AI developers can design applications with change in mind, allowing model updates on a separate channel than code and including mechanisms to monitor the model’s performance and outputs.

Model integration risks: insecure integrated system, model reverse engineering, denial-of-service attacks, model source tampering

The integration point introduces several security risks for application creators. Data could be leaked due to an insecure integration, the model itself could be reverse engineered, or malicious users could launch denial-of-service attacks. Updates may introduce supply chain risks or incompatibilities. Thorough testing and debugging are essential to mitigate these risks.

Many traditional web security vulnerabilities also apply to AI applications. Insecure backend API integration or web frameworks could lead to the interception of data passing between the application and API. This risk of an insecure integrated system can be severe for AI applications, given the nature of the data they often handle. LLM prompts can be much longer than a typical web query and may contain sensitive data like emails or code.

Furthermore, applications integrated with a model might store queries and response logs, potentially including sensitive data from integrated plugins such as calendar entries. Some generative AI applications store user interactions for model refinement, introducing another avenue for data leakage in the event of storage vulnerabilities. Finally, practitioners should be aware that generative AI APIs used by developers may also have their own logging behavior separate from the core application.

If an application has unrestricted access to the model, an attacker using the application could exploit this access. For example, a malicious actor might try to use a model intended only for reading documents to delete them instead. Limiting access, implementing authentication, and enforcing authorization are crucial for controlling how the application interacts with the model.

Conversely, a user could try to manipulate an application’s integration to extract information about the model itself. Without rate limits on queries, a persistent actor could potentially **reverse engineer** the model by sending numerous requests and analyzing the responses. Likewise, they could attempt **denial-of-service attacks** by flooding the model with too many requests, if requests aren’t rate limited or load balanced.

Finally, updates can cause [_architectural drift_](https://www.crowdstrike.com/blog/architecture-drift/). New model versions might use updated frameworks or have different architectures, potentially causing incompatibility with the serving environment. Applications may allow versioning and compatibility in a range of model architecture versions. Developers should also be aware of risks from updating a model too early or from untrusted sources: the new model might be malicious, tampered with, or not yet adequately tested yet. Checking the model card and model provenance can help avoid updating to a model that is not yet production ready.

##  Application testing

### Application testing

As with traditional software, testing and debugging is an essential part of AI development. However, AI development introduces unique challenges due to the non-deterministic nature of AI models. Unlike traditional software with predictable behavior and failure models, AI backends can exhibit stochastic (random) behaviors. This makes them difficult to test with traditional methods like unit tests, and errors may not be easily reproducible. Furthermore, the inner workings of AI models are often opaque, making them hard to review and fully understand.

“AI development introduces unique challenges due to the non-deterministic nature of AI models.”

Considering these complexities, testing might evaluate the system's behavior within acceptable ranges, rather than aiming for precise output matching. For example, developers might create unit or integration tests that simulate known adversarial inputs and confirm that the system doesn’t produce harmful outputs. These “golden master tests” can establish and maintain a record of security and safety parameters early in the development process, potentially preventing regressions later.

They may also use fuzz testing on the prompts, sending random strings to the model and analyzing the outputs (or distribution of the outputs) to be sure no harmful output is produced. Ideally, the model would respond with a standard error message if the prompt is nonsense, but given the potential of prompt injection, testing with random inputs may still yield useful results.

Because testing is most effective when done in the context of the entire application stack, rather than focusing solely on the model in isolation, AI developers should include testing or adversarial attacks throughout the development process.

  * ![](https://www.gstatic.com/marketing-cms/assets/images/e9/bc/394093d7467588f812f19c1b266d/g-shield-lockup-footer.svg)



