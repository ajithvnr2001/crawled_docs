---
url: https://developer.android.com/kotlin/ktx/extensions-list/
title: List of KTX extensions \u00a0|\u00a0 Kotlin \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:26.258361+00:00
---

# List of KTX extensions  |  Kotlin  |  Android Developers

> Source: https://developer.android.com/kotlin/ktx/extensions-list/

  * [ Android Developers ](https://developer.android.com/)
  * [ Get started ](https://developer.android.com/get-started/overview)
  * [ Kotlin ](https://developer.android.com/kotlin)
  * [ Guides ](https://developer.android.com/kotlin/first)



#  List of KTX extensions Stay organized with collections  Save and categorize content based on your preferences. 

## androidx.activity

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.activity:activity-ktx:1.13.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.activity:activity-ktx:1.13.0")
    }

#### Extension functions

##### For [OnBackPressedDispatcher](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedDispatcher)

[OnBackPressedCallback](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback) |  `[OnBackPressedDispatcher](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedDispatcher).[addCallback](https://developer.android.com/reference/kotlin/androidx/activity/package-summary#\(androidx.activity.OnBackPressedDispatcher\).addCallback\(androidx.lifecycle.LifecycleOwner,%20kotlin.Boolean,%20kotlin.Function1\))(owner: [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)? = null, enabled: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = true, onBackPressed: [OnBackPressedCallback](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Create and add a new [OnBackPressedCallback](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback) that calls onBackPressed in [OnBackPressedCallback.handleOnBackPressed](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback#handleOnBackPressed\(\)).  
---|---  
  
##### For [ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)

[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> |  `[ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity).[viewModels](https://developer.android.com/reference/kotlin/androidx/activity/package-summary#\(androidx.activity.ComponentActivity\).viewModels\(kotlin.Function0,kotlin.Function0\))(noinline factoryProducer: () -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) = null)` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the ComponentActivity's ViewModel, if factoryProducer is specified then [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) first time.  
---|---  
  
## androidx.benchmark

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.benchmark:benchmark-junit4:1.5.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.benchmark:benchmark-junit4:1.5.0")
    }

#### Top-level functions

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[beginTraceSection](https://developer.android.com/reference/kotlin/androidx/benchmark/package-summary)(sectionName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/))`  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[endTraceSection](https://developer.android.com/reference/kotlin/androidx/benchmark/package-summary)()`  
  
## androidx.benchmark.junit4

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.benchmark:benchmark-junit4:1.5.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.benchmark:benchmark-junit4:1.5.0")
    }

#### Extension functions

##### For [BenchmarkRule](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[BenchmarkRule](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule).[measureRepeated](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/package-summary#\(androidx.benchmark.junit4.BenchmarkRule\).measureRepeated\(kotlin.Function1\))(crossinline block: [BenchmarkRule.Scope](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule.Scope).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Benchmark a block of code.  
---|---  
  
## androidx.collection

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.collection:collection-ktx:1.7.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.collection:collection-ktx:1.7.0")
    }

#### Extension functions

##### For [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[contains](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).contains\(kotlin.Long\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Returns true if the collection contains key.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[forEach](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).forEach\(kotlin.Function2\))(action: (key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), value: T) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action for each key/value entry.  
T |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[getOrDefault](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).getOrDefault\(kotlin.Long,kotlin.Any\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), defaultValue: T)` Return the value corresponding to key, or defaultValue when not present.  
T |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[getOrElse](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).getOrElse\(kotlin.Long,%20kotlin.Function0\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), defaultValue: () -> T)` Return the value corresponding to key, or from defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).isNotEmpty\(\))()` Return true when the collection contains elements.  
[LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[keyIterator](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).keyIterator\(\))()` Return an iterator over the collection's keys.  
operator [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T> |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[plus](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).plus\(androidx.collection.LongSparseArray\))(other: [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>)` Creates a new collection by adding or replacing entries from other.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[remove](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray#remove\(kotlin.Long,kotlin.Any\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), value: T)` Removes the entry for key only if it is mapped to value.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[set](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).set\(kotlin.Long,kotlin.Any\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), value: T)` Allows the use of the index operator for storing values in the collection.  
[Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[valueIterator](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).valueIterator\(\))()` Return an iterator over the collection's values.  
  
##### For [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[contains](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).contains\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[forEach](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).forEach\(kotlin.Function2\))(action: (key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: T) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action for each key/value entry.  
T |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[getOrDefault](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).getOrDefault\(kotlin.Int,kotlin.Any\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: T)` Return the value corresponding to key, or defaultValue when not present.  
T |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[getOrElse](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).getOrElse\(kotlin.Int,%20kotlin.Function0\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: () -> T)` Return the value corresponding to key, or from defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).isNotEmpty\(\))()` Return true when the collection contains elements.  
[IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[keyIterator](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).keyIterator\(\))()` Return an iterator over the collection's keys.  
operator [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T> |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[plus](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).plus\(androidx.collection.SparseArrayCompat\))(other: [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>)` Creates a new collection by adding or replacing entries from other.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[remove](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat#remove\(kotlin.Int,kotlin.Any\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: T)` Removes the entry for key only if it is mapped to value.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[set](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).set\(kotlin.Int,kotlin.Any\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: T)` Allows the use of the index operator for storing values in the collection.  
[Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[valueIterator](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).valueIterator\(\))()` Return an iterator over the collection's values.  
  
#### Extension properties

##### For [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)<T>.[size](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.LongSparseArray\).size\(\))()` Returns the number of key/value pairs in the collection.  
---|---  
  
##### For [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)<T>.[size](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#\(androidx.collection.SparseArrayCompat\).size\(\))()` Returns the number of key/value pairs in the collection.  
---|---  
  
#### Top-level functions

[ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap)<K, V> |  `[arrayMapOf](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arrayMapOf\(\))()` Returns an empty new [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap).  
---|---  
[ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap)<K, V> |  `[arrayMapOf](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arrayMapOf\(kotlin.Array\))(vararg pairs: [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<K, V>)` Returns a new [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap) with the specified contents, given as a list of pairs where the first component is the key and the second component is the value.  
[ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet)<T> |  `[arraySetOf](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arraySetOf\(\))()` Returns an empty new [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet).  
[ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet)<T> |  `[arraySetOf](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arraySetOf\(kotlin.Array\))(vararg values: T)` Returns a new [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet) with the specified contents.  
[LruCache](https://developer.android.com/reference/kotlin/androidx/collection/LruCache)<K, V> |  `[lruCache](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#lruCache\(kotlin.Int,%20kotlin.Function2,%20kotlin.Function1,%20kotlin.Function4\))(maxSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), crossinline sizeOf: (key: K, value: V) -> [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/), key: K, oldValue: V, newValue: V?) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = { _, _, _, _ -> })` Creates an [LruCache](https://developer.android.com/reference/kotlin/androidx/collection/LruCache) with the given parameters.  
  
## androidx.core.animation

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.animation.Animator](https://developer.android.com/reference/android/animation/Animator)

[AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[addListener](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).addListener\(kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1\))(crossinline onEnd: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onStart: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onCancel: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onRepeat: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {})` Add a listener to this Animator using the provided actions.  
---|---  
[AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator.AnimatorPauseListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[addPauseListener](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).addPauseListener\(kotlin.Function1,%20kotlin.Function1\))(crossinline onResume: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onPause: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {})` Add a pause and resume listener to this Animator using the provided actions.  
[AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[doOnCancel](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).doOnCancel\(kotlin.Function1\))(crossinline action: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when the animation has been cancelled.  
[AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[doOnEnd](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).doOnEnd\(kotlin.Function1\))(crossinline action: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when the animation has ended.  
[AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator.AnimatorPauseListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[doOnPause](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).doOnPause\(kotlin.Function1\))(crossinline action: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when the animation has been paused.  
[AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[doOnRepeat](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).doOnRepeat\(kotlin.Function1\))(crossinline action: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when the animation has repeated.  
[AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator.AnimatorPauseListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[doOnResume](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).doOnResume\(kotlin.Function1\))(crossinline action: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when the animation has resumed after a pause.  
[AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener) |  `[Animator](https://developer.android.com/reference/android/animation/Animator).[doOnStart](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#\(android.animation.Animator\).doOnStart\(kotlin.Function1\))(crossinline action: (animator: [Animator](https://developer.android.com/reference/android/animation/Animator)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when the animation has started.  
  
## androidx.core.content

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.content.Context](https://developer.android.com/reference/android/content/Context)

T? |  `[Context](https://developer.android.com/reference/android/content/Context).[getSystemService](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#\(android.content.Context\).getSystemService\(\))()` Return the handle to a system-level service by class.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Context](https://developer.android.com/reference/android/content/Context).[withStyledAttributes](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#\(android.content.Context\).withStyledAttributes\(android.util.AttributeSet,%20kotlin.IntArray,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1\))(set: [AttributeSet](https://developer.android.com/reference/android/util/AttributeSet)? = null, attrs: [IntArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int-array/), @AttrRes defStyleAttr: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 0, @StyleRes defStyleRes: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 0, block: [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Executes block on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray) receiver.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Context](https://developer.android.com/reference/android/content/Context).[withStyledAttributes](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#\(android.content.Context\).withStyledAttributes\(kotlin.Int,%20kotlin.IntArray,%20kotlin.Function1\))(@StyleRes resourceId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), attrs: [IntArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int-array/), block: [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Executes block on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray) receiver.  
  
##### For [android.content.SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences).[edit](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#\(android.content.SharedPreferences\).edit\(kotlin.Boolean,%20kotlin.Function1\))(commit: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = false, action: [Editor](https://developer.android.com/reference/android/content/SharedPreferences.Editor).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Allows editing of this preference instance with a call to [apply](https://developer.android.com/reference/android/content/SharedPreferences.Editor#apply\(\)) or [commit](https://developer.android.com/reference/android/content/SharedPreferences.Editor#commit\(\)) to persist the changes.  
---|---  
  
#### Top-level functions

[ContentValues](https://developer.android.com/reference/android/content/ContentValues) |  `[contentValuesOf](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#contentValuesOf\(kotlin.Array\))(vararg pairs: [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/)?>)` Returns a new [ContentValues](https://developer.android.com/reference/android/content/ContentValues) with the given key/value pairs as elements.  
---|---  
  
## androidx.core.content.res

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.content.res.TypedArray](https://developer.android.com/reference/android/content/res/TypedArray)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getBooleanOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getBooleanOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the boolean value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
---|---  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getColorOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getColorOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the color value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getColorStateListOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getColorStateListOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the color state list value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getDimensionOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getDimensionOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the dimension value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getDimensionPixelOffsetOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getDimensionPixelOffsetOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the dimension pixel offset value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getDimensionPixelSizeOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getDimensionPixelSizeOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the dimension pixel size value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getDrawableOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getDrawableOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the drawable value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getFloatOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getFloatOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the float value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Typeface](https://developer.android.com/reference/android/graphics/Typeface) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getFontOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getFontOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the font value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getIntOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getIntOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the integer value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getIntegerOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getIntegerOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the integer value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getResourceIdOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getResourceIdOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieves the resource identifier for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getStringOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getStringOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the string value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/)<[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)> |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getTextArrayOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getTextArrayOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the text array value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[getTextOrThrow](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).getTextOrThrow\(kotlin.Int\))(@StyleableRes index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Retrieve the text value for the attribute at index or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined.  
R |  `[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).[use](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#\(android.content.res.TypedArray\).use\(kotlin.Function1\))(block: ([TypedArray](https://developer.android.com/reference/android/content/res/TypedArray)) -> R)` Executes the given block function on this TypedArray and then recycles it.  
  
## androidx.core.database

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.database.Cursor](https://developer.android.com/reference/android/database/Cursor)

[ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/)? |  `[Cursor](https://developer.android.com/reference/android/database/Cursor).[getBlobOrNull](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#\(android.database.Cursor\).getBlobOrNull\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the requested column as a nullable byte array.  
---|---  
[Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/)? |  `[Cursor](https://developer.android.com/reference/android/database/Cursor).[getDoubleOrNull](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#\(android.database.Cursor\).getDoubleOrNull\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the requested column as a nullable double.  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)? |  `[Cursor](https://developer.android.com/reference/android/database/Cursor).[getFloatOrNull](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#\(android.database.Cursor\).getFloatOrNull\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the requested column as a nullable float.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)? |  `[Cursor](https://developer.android.com/reference/android/database/Cursor).[getIntOrNull](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#\(android.database.Cursor\).getIntOrNull\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the requested column as a nullable integer.  
[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)? |  `[Cursor](https://developer.android.com/reference/android/database/Cursor).[getLongOrNull](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#\(android.database.Cursor\).getLongOrNull\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the requested column as a nullable long.  
[Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/)? |  `[Cursor](https://developer.android.com/reference/android/database/Cursor).[getShortOrNull](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#\(android.database.Cursor\).getShortOrNull\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the requested column as a nullable short.  
[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)? |  `[Cursor](https://developer.android.com/reference/android/database/Cursor).[getStringOrNull](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#\(android.database.Cursor\).getStringOrNull\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the requested column as a nullable string.  
  
## androidx.core.database.sqlite

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.database.sqlite.SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase)

T |  `[SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase).[transaction](https://developer.android.com/reference/kotlin/androidx/core/database/sqlite/package-summary#\(android.database.sqlite.SQLiteDatabase\).transaction\(kotlin.Boolean,%20kotlin.Function1\))(exclusive: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = true, body: [SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase).() -> T)` Run body in a transaction marking it as successful if it completes without exception.  
---|---  
  
## androidx.core.graphics

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap)

[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[applyCanvas](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Bitmap\).applyCanvas\(kotlin.Function1\))(block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas) to draw on this bitmap and executes the specified block on the newly created canvas.  
---|---  
operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[contains](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Bitmap\).contains\(android.graphics.Point\))(p: [Point](https://developer.android.com/reference/android/graphics/Point))` Returns true if the specified point is inside the bitmap.  
operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[contains](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Bitmap\).contains\(android.graphics.PointF\))(p: [PointF](https://developer.android.com/reference/android/graphics/PointF))` Returns true if the specified point is inside the bitmap.  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[get](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Bitmap\).get\(kotlin.Int,%20kotlin.Int\))(x: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), y: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the value of the pixel at the specified location.  
[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[scale](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Bitmap\).scale\(kotlin.Int,%20kotlin.Int,%20kotlin.Boolean\))(width: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), height: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), filter: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = true)` Creates a new bitmap, scaled from this bitmap, when possible.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[set](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Bitmap\).set\(kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(x: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), y: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), color: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Writes the specified [color int](https://developer.android.com/reference/android/graphics/Color) into the bitmap (assuming it is mutable) at the specified `(x, y)` coordinate.  
  
##### For [android.graphics.Canvas](https://developer.android.com/reference/android/graphics/Canvas)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withClip](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withClip\(android.graphics.Rect,%20kotlin.Function1\))(clipRect: [Rect](https://developer.android.com/reference/android/graphics/Rect), block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas#clipRect\(android.graphics.RectF,%20android.graphics.Region.Op\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withClip](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withClip\(android.graphics.RectF,%20kotlin.Function1\))(clipRect: [RectF](https://developer.android.com/reference/android/graphics/RectF), block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas#clipRect\(android.graphics.RectF,%20android.graphics.Region.Op\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withClip](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withClip\(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1\))(left: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), top: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), right: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), bottom: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas#clipRect\(android.graphics.RectF,%20android.graphics.Region.Op\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withClip](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withClip\(kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1\))(left: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/), top: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/), right: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/), bottom: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/), block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas#clipRect\(android.graphics.RectF,%20android.graphics.Region.Op\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withClip](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withClip\(android.graphics.Path,%20kotlin.Function1\))(clipPath: [Path](https://developer.android.com/reference/android/graphics/Path), block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.clipPath](https://developer.android.com/reference/android/graphics/Canvas#clipPath\(android.graphics.Path,%20android.graphics.Region.Op\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withMatrix](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withMatrix\(android.graphics.Matrix,%20kotlin.Function1\))(matrix: [Matrix](https://developer.android.com/reference/android/graphics/Matrix) = Matrix(), block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.concat](https://developer.android.com/reference/android/graphics/Canvas#concat\(android.graphics.Matrix\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withRotation](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withRotation\(kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1\))(degrees: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, pivotX: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, pivotY: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.rotate](https://developer.android.com/reference/android/graphics/Canvas#rotate\(float\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withSave](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withSave\(kotlin.Function1\))(block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withScale](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withScale\(kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1\))(x: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 1.0f, y: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 1.0f, pivotX: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, pivotY: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.scale](https://developer.android.com/reference/android/graphics/Canvas#scale\(float,%20float\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withSkew](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withSkew\(kotlin.Float,%20kotlin.Float,%20kotlin.Function1\))(x: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, y: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.skew](https://developer.android.com/reference/android/graphics/Canvas#skew\(float,%20float\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Canvas](https://developer.android.com/reference/android/graphics/Canvas).[withTranslation](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Canvas\).withTranslation\(kotlin.Float,%20kotlin.Float,%20kotlin.Function1\))(x: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, y: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas#save\(\))/[Canvas.translate](https://developer.android.com/reference/android/graphics/Canvas#translate\(float,%20float\)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas#restoreToCount\(int\)).  
  
##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color)

operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Color](https://developer.android.com/reference/android/graphics/Color).[component1](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Color\).component1\(\))()` Returns the first component of the color.  
---|---  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Color](https://developer.android.com/reference/android/graphics/Color).[component2](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Color\).component2\(\))()` Returns the second component of the color.  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Color](https://developer.android.com/reference/android/graphics/Color).[component3](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Color\).component3\(\))()` Returns the third component of the color.  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Color](https://developer.android.com/reference/android/graphics/Color).[component4](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Color\).component4\(\))()` Returns the fourth component of the color.  
infix [Color](https://developer.android.com/reference/android/graphics/Color)! |  `[Color](https://developer.android.com/reference/android/graphics/Color).[convertTo](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Color\).convertTo\(android.graphics.ColorSpace.Named\))(colorSpace: [Named](https://developer.android.com/reference/android/graphics/ColorSpace.Named))` Converts the color receiver to a color in the specified color space.  
infix [Color](https://developer.android.com/reference/android/graphics/Color)! |  `[Color](https://developer.android.com/reference/android/graphics/Color).[convertTo](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Color\).convertTo\(android.graphics.ColorSpace\))(colorSpace: [ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace))` Converts the color receiver to a color in the specified color space.  
operator [Color](https://developer.android.com/reference/android/graphics/Color) |  `[Color](https://developer.android.com/reference/android/graphics/Color).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Color\).plus\(android.graphics.Color\))(c: [Color](https://developer.android.com/reference/android/graphics/Color))` Composites two translucent colors together.  
  
##### For [android.graphics.ImageDecoder.Source](https://developer.android.com/reference/android/graphics/ImageDecoder.Source)

[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) |  `[Source](https://developer.android.com/reference/android/graphics/ImageDecoder.Source).[decodeBitmap](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.ImageDecoder.Source\).decodeBitmap\(kotlin.Function3\))(crossinline action: [ImageDecoder](https://developer.android.com/reference/android/graphics/ImageDecoder).(info: [ImageInfo](https://developer.android.com/reference/android/graphics/ImageDecoder.ImageInfo), source: [Source](https://developer.android.com/reference/android/graphics/ImageDecoder.Source)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Create a Bitmap from a Source  
---|---  
[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) |  `[Source](https://developer.android.com/reference/android/graphics/ImageDecoder.Source).[decodeDrawable](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.ImageDecoder.Source\).decodeDrawable\(kotlin.Function3\))(crossinline action: [ImageDecoder](https://developer.android.com/reference/android/graphics/ImageDecoder).(info: [ImageInfo](https://developer.android.com/reference/android/graphics/ImageDecoder.ImageInfo), source: [Source](https://developer.android.com/reference/android/graphics/ImageDecoder.Source)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Create a Drawable from a Source  
  
##### For [android.graphics.Matrix](https://developer.android.com/reference/android/graphics/Matrix)

operator [Matrix](https://developer.android.com/reference/android/graphics/Matrix) |  `[Matrix](https://developer.android.com/reference/android/graphics/Matrix).[times](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Matrix\).times\(android.graphics.Matrix\))(m: [Matrix](https://developer.android.com/reference/android/graphics/Matrix))` Multiplies this [Matrix](https://developer.android.com/reference/android/graphics/Matrix) by another matrix and returns the result as a new matrix.  
---|---  
[FloatArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array/) |  `[Matrix](https://developer.android.com/reference/android/graphics/Matrix).[values](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Matrix\).values\(\))()` Returns the 9 values of this [Matrix](https://developer.android.com/reference/android/graphics/Matrix) as a new array of floats.  
  
##### For [android.graphics.Paint](https://developer.android.com/reference/android/graphics/Paint)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Paint](https://developer.android.com/reference/android/graphics/Paint).[setBlendMode](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Paint\).setBlendMode\(androidx.core.graphics.BlendModeCompat\))(blendModeCompat: [BlendModeCompat](https://developer.android.com/reference/kotlin/androidx/core/graphics/BlendModeCompat)?)` Convenience method to configure the BlendMode of a Paint in a backward compatible way.  
---|---  
  
##### For [android.graphics.Path](https://developer.android.com/reference/android/graphics/Path)

infix [Path](https://developer.android.com/reference/android/graphics/Path) |  `[Path](https://developer.android.com/reference/android/graphics/Path).[and](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Path\).and\(android.graphics.Path\))(p: [Path](https://developer.android.com/reference/android/graphics/Path))` Returns the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path).  
---|---  
[Iterable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/)<[PathSegment](https://developer.android.com/reference/kotlin/androidx/core/graphics/PathSegment)> |  `[Path](https://developer.android.com/reference/android/graphics/Path).[flatten](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Path\).flatten\(kotlin.Float\))(error: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.5f)` Flattens (or approximate) the [Path](https://developer.android.com/reference/android/graphics/Path) with a series of line segments.  
operator [Path](https://developer.android.com/reference/android/graphics/Path) |  `[Path](https://developer.android.com/reference/android/graphics/Path).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Path\).minus\(android.graphics.Path\))(p: [Path](https://developer.android.com/reference/android/graphics/Path))` Returns the difference of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path).  
infix [Path](https://developer.android.com/reference/android/graphics/Path) |  `[Path](https://developer.android.com/reference/android/graphics/Path).[or](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Path\).or\(android.graphics.Path\))(p: [Path](https://developer.android.com/reference/android/graphics/Path))` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path).  
operator [Path](https://developer.android.com/reference/android/graphics/Path) |  `[Path](https://developer.android.com/reference/android/graphics/Path).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Path\).plus\(android.graphics.Path\))(p: [Path](https://developer.android.com/reference/android/graphics/Path))` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path).  
infix [Path](https://developer.android.com/reference/android/graphics/Path) |  `[Path](https://developer.android.com/reference/android/graphics/Path).[xor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Path\).xor\(android.graphics.Path\))(p: [Path](https://developer.android.com/reference/android/graphics/Path))` Returns the union minus the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path).  
  
##### For [android.graphics.Picture](https://developer.android.com/reference/android/graphics/Picture)

[Picture](https://developer.android.com/reference/android/graphics/Picture) |  `[Picture](https://developer.android.com/reference/android/graphics/Picture).[record](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Picture\).record\(kotlin.Int,%20kotlin.Int,%20kotlin.Function1\))(width: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), height: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), block: [Canvas](https://developer.android.com/reference/android/graphics/Canvas).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas) to record commands in this [Picture](https://developer.android.com/reference/android/graphics/Picture), executes the specified block on the newly created canvas and returns this [Picture](https://developer.android.com/reference/android/graphics/Picture).  
---|---  
  
##### For [android.graphics.Point](https://developer.android.com/reference/android/graphics/Point)

operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[component1](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).component1\(\))()` Returns the x coordinate of this point.  
---|---  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[component2](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).component2\(\))()` Returns the y coordinate of this point.  
operator [Point](https://developer.android.com/reference/android/graphics/Point) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).minus\(android.graphics.Point\))(p: [Point](https://developer.android.com/reference/android/graphics/Point))` Offsets this point by the negation of the specified point and returns the result as a new point.  
operator [Point](https://developer.android.com/reference/android/graphics/Point) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).minus\(kotlin.Int\))(xy: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point.  
operator [Point](https://developer.android.com/reference/android/graphics/Point) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).plus\(android.graphics.Point\))(p: [Point](https://developer.android.com/reference/android/graphics/Point))` Offsets this point by the specified point and returns the result as a new point.  
operator [Point](https://developer.android.com/reference/android/graphics/Point) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).plus\(kotlin.Int\))(xy: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point.  
[PointF](https://developer.android.com/reference/android/graphics/PointF) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[toPointF](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).toPointF\(\))()` Returns a [PointF](https://developer.android.com/reference/android/graphics/PointF) representation of this point.  
operator [Point](https://developer.android.com/reference/android/graphics/Point) |  `[Point](https://developer.android.com/reference/android/graphics/Point).[unaryMinus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Point\).unaryMinus\(\))()` Returns a new point representing the negation of this point.  
  
##### For [android.graphics.PointF](https://developer.android.com/reference/android/graphics/PointF)

operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[component1](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).component1\(\))()` Returns the x coordinate of this point.  
---|---  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[component2](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).component2\(\))()` Returns the y coordinate of this point.  
operator [PointF](https://developer.android.com/reference/android/graphics/PointF) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).minus\(android.graphics.PointF\))(p: [PointF](https://developer.android.com/reference/android/graphics/PointF))` Offsets this point by the negation of the specified point and returns the result as a new point.  
operator [PointF](https://developer.android.com/reference/android/graphics/PointF) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).minus\(kotlin.Float\))(xy: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/))` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point.  
operator [PointF](https://developer.android.com/reference/android/graphics/PointF) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).plus\(android.graphics.PointF\))(p: [PointF](https://developer.android.com/reference/android/graphics/PointF))` Offsets this point by the specified point and returns the result as a new point.  
operator [PointF](https://developer.android.com/reference/android/graphics/PointF) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).plus\(kotlin.Float\))(xy: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/))` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point.  
[Point](https://developer.android.com/reference/android/graphics/Point) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[toPoint](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).toPoint\(\))()` Returns a [Point](https://developer.android.com/reference/android/graphics/Point) representation of this point.  
operator [PointF](https://developer.android.com/reference/android/graphics/PointF) |  `[PointF](https://developer.android.com/reference/android/graphics/PointF).[unaryMinus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PointF\).unaryMinus\(\))()` Returns a new point representing the negation of this point.  
  
##### For [android.graphics.PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode)

[PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter) |  `[Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode).[toColorFilter](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PorterDuff.Mode\).toColorFilter\(kotlin.Int\))(color: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Creates a new [PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode) as the alpha compositing or blending mode, and the specified color.  
---|---  
[PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode) |  `[Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode).[toXfermode](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.PorterDuff.Mode\).toXfermode\(\))()` Creates a new [PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode) as the alpha compositing or blending mode.  
  
##### For [android.graphics.Rect](https://developer.android.com/reference/android/graphics/Rect)

infix [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[and](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).and\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Returns the intersection of two rectangles as a new rectangle.  
---|---  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[component1](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).component1\(\))()` Returns "left", the first component of the rectangle.  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[component2](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).component2\(\))()` Returns "top", the second component of the rectangle.  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[component3](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).component3\(\))()` Returns "right", the third component of the rectangle.  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[component4](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).component4\(\))()` Returns "bottom", the fourth component of the rectangle.  
operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[contains](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).contains\(android.graphics.Point\))(p: [Point](https://developer.android.com/reference/android/graphics/Point))` Returns true if the specified point is inside the rectangle.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).minus\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Returns the difference of this rectangle and the specified rectangle as a new region.  
operator [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).minus\(kotlin.Int\))(xy: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis.  
operator [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).minus\(android.graphics.Point\))(xy: [Point](https://developer.android.com/reference/android/graphics/Point))` Returns a new rectangle representing this rectangle offset by the negation of the specified point.  
infix [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[or](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).or\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Returns the union of two rectangles as a new rectangle.  
operator [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).plus\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle.  
operator [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).plus\(kotlin.Int\))(xy: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis.  
operator [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).plus\(android.graphics.Point\))(xy: [Point](https://developer.android.com/reference/android/graphics/Point))` Returns a new rectangle representing this rectangle offset by the specified point.  
operator [Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[times](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).times\(kotlin.Int\))(factor: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns a new rectangle representing this rectangle's components each scaled by factor.  
[RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[toRectF](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).toRectF\(\))()` Returns a [RectF](https://developer.android.com/reference/android/graphics/RectF) representation of this rectangle.  
[Region](https://developer.android.com/reference/android/graphics/Region) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[toRegion](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).toRegion\(\))()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region) representation of this rectangle.  
infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Rect](https://developer.android.com/reference/android/graphics/Rect).[xor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Rect\).xor\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Returns the union minus the intersection of two rectangles as a new region.  
  
##### For [android.graphics.RectF](https://developer.android.com/reference/android/graphics/RectF)

infix [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[and](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).and\(android.graphics.RectF\))(r: [RectF](https://developer.android.com/reference/android/graphics/RectF))` Returns the intersection of two rectangles as a new rectangle.  
---|---  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[component1](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).component1\(\))()` Returns "left", the first component of the rectangle.  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[component2](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).component2\(\))()` Returns "top", the second component of the rectangle.  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[component3](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).component3\(\))()` Returns "right", the third component of the rectangle.  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[component4](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).component4\(\))()` Returns "bottom", the fourth component of the rectangle.  
operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[contains](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).contains\(android.graphics.PointF\))(p: [PointF](https://developer.android.com/reference/android/graphics/PointF))` Returns true if the specified point is inside the rectangle.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).minus\(android.graphics.RectF\))(r: [RectF](https://developer.android.com/reference/android/graphics/RectF))` Returns the difference of this rectangle and the specified rectangle as a new region.  
operator [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).minus\(kotlin.Float\))(xy: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/))` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis.  
operator [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).minus\(android.graphics.PointF\))(xy: [PointF](https://developer.android.com/reference/android/graphics/PointF))` Returns a new rectangle representing this rectangle offset by the negation of the specified point.  
infix [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[or](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).or\(android.graphics.RectF\))(r: [RectF](https://developer.android.com/reference/android/graphics/RectF))` Returns the union of two rectangles as a new rectangle.  
operator [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).plus\(android.graphics.RectF\))(r: [RectF](https://developer.android.com/reference/android/graphics/RectF))` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle.  
operator [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).plus\(kotlin.Float\))(xy: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/))` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis.  
operator [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).plus\(android.graphics.PointF\))(xy: [PointF](https://developer.android.com/reference/android/graphics/PointF))` Returns a new rectangle representing this rectangle offset by the specified point.  
operator [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[times](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).times\(kotlin.Int\))(factor: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns a new rectangle representing this rectangle's components each scaled by factor.  
operator [RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[times](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).times\(kotlin.Float\))(factor: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/))` Returns a new rectangle representing this rectangle's components each scaled by factor.  
[Rect](https://developer.android.com/reference/android/graphics/Rect) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[toRect](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).toRect\(\))()` Returns a [Rect](https://developer.android.com/reference/android/graphics/Rect) representation of this rectangle.  
[Region](https://developer.android.com/reference/android/graphics/Region) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[toRegion](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).toRegion\(\))()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region) representation of this rectangle.  
[RectF](https://developer.android.com/reference/android/graphics/RectF) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[transform](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).transform\(android.graphics.Matrix\))(m: [Matrix](https://developer.android.com/reference/android/graphics/Matrix))` Transform this rectangle in place using the supplied [Matrix](https://developer.android.com/reference/android/graphics/Matrix) and returns this rectangle.  
infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[RectF](https://developer.android.com/reference/android/graphics/RectF).[xor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.RectF\).xor\(android.graphics.RectF\))(r: [RectF](https://developer.android.com/reference/android/graphics/RectF))` Returns the union minus the intersection of two rectangles as a new region.  
  
##### For [android.graphics.Region](https://developer.android.com/reference/android/graphics/Region)

infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[and](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).and\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Return the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect) as a new region.  
---|---  
infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[and](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).and\(android.graphics.Region\))(r: [Region](https://developer.android.com/reference/android/graphics/Region))` Return the intersection of this region and the specified region as a new region.  
operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[contains](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).contains\(android.graphics.Point\))(p: [Point](https://developer.android.com/reference/android/graphics/Point))` Return true if the region contains the specified [Point](https://developer.android.com/reference/android/graphics/Point).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[forEach](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).forEach\(kotlin.Function1\))(action: (rect: [Rect](https://developer.android.com/reference/android/graphics/Rect)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action on each rect in this region.  
operator [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<[Rect](https://developer.android.com/reference/android/graphics/Rect)> |  `[Region](https://developer.android.com/reference/android/graphics/Region).[iterator](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).iterator\(\))()` Returns an [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/) over the rects in this region.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).minus\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Return the difference of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect) as a new region.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[minus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).minus\(android.graphics.Region\))(r: [Region](https://developer.android.com/reference/android/graphics/Region))` Return the difference of this region and the specified region as a new region.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[not](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).not\(\))()` Returns the negation of this region as a new region.  
infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[or](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).or\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect) as a new region.  
infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[or](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).or\(android.graphics.Region\))(r: [Region](https://developer.android.com/reference/android/graphics/Region))` Return the union of this region and the specified region as a new region.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).plus\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect) as a new region.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[plus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).plus\(android.graphics.Region\))(r: [Region](https://developer.android.com/reference/android/graphics/Region))` Return the union of this region and the specified region as a new region.  
operator [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[unaryMinus](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).unaryMinus\(\))()` Returns the negation of this region as a new region.  
infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[xor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).xor\(android.graphics.Rect\))(r: [Rect](https://developer.android.com/reference/android/graphics/Rect))` Return the union minus the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect) as a new region.  
infix [Region](https://developer.android.com/reference/android/graphics/Region) |  `[Region](https://developer.android.com/reference/android/graphics/Region).[xor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Region\).xor\(android.graphics.Region\))(r: [Region](https://developer.android.com/reference/android/graphics/Region))` Return the union minus the intersection of this region and the specified region as a new region.  
  
##### For [android.graphics.Shader](https://developer.android.com/reference/android/graphics/Shader)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Shader](https://developer.android.com/reference/android/graphics/Shader).[transform](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(android.graphics.Shader\).transform\(kotlin.Function1\))(block: [Matrix](https://developer.android.com/reference/android/graphics/Matrix).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap the specified block in calls to [Shader.getLocalMatrix](https://developer.android.com/reference/android/graphics/Shader#getLocalMatrix\(android.graphics.Matrix\)) and [Shader.setLocalMatrix](https://developer.android.com/reference/android/graphics/Shader#setLocalMatrix\(android.graphics.Matrix\)).  
---|---  
  
##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[component1](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).component1\(\))()` Return the alpha component of a color int.  
---|---  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[component2](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).component2\(\))()` Return the red component of a color int.  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[component3](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).component3\(\))()` Return the green component of a color int.  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[component4](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).component4\(\))()` Return the blue component of a color int.  
infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[convertTo](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).convertTo\(android.graphics.ColorSpace.Named\))(colorSpace: [Named](https://developer.android.com/reference/android/graphics/ColorSpace.Named))` Converts the color int receiver to a color long in the specified color space.  
infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[convertTo](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).convertTo\(android.graphics.ColorSpace\))(colorSpace: [ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace))` Converts the color int receiver to a color long in the specified color space.  
[Color](https://developer.android.com/reference/android/graphics/Color) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[toColor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).toColor\(\))()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color) instance from a color int.  
[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[toColorLong](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).toColorLong\(\))()` Converts the specified ARGB [color int](https://developer.android.com/reference/android/graphics/Color) to an RGBA [color long](https://developer.android.com/reference/android/graphics/Color) in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace.Named#SRGB) color space.  
  
##### For [kotlin.Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)

operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[component1](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).component1\(\))()` Returns the first component of the color.  
---|---  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[component2](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).component2\(\))()` Returns the second component of the color.  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[component3](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).component3\(\))()` Returns the third component of the color.  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[component4](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).component4\(\))()` Returns the fourth component of the color.  
infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[convertTo](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).convertTo\(android.graphics.ColorSpace.Named\))(colorSpace: [Named](https://developer.android.com/reference/android/graphics/ColorSpace.Named))` Converts the color long receiver to a color long in the specified color space.  
infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[convertTo](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).convertTo\(android.graphics.ColorSpace\))(colorSpace: [ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace))` Converts the color long receiver to a color long in the specified color space.  
[Color](https://developer.android.com/reference/android/graphics/Color) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[toColor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).toColor\(\))()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color) instance from a [color long](https://developer.android.com/reference/android/graphics/Color).  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[toColorInt](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).toColorInt\(\))()` Converts the specified [color long](https://developer.android.com/reference/android/graphics/Color) to an ARGB [color int](https://developer.android.com/reference/android/graphics/Color).  
  
##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).[toColorInt](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.String\).toColorInt\(\))()` Return a corresponding [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) color of this [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).  
---|---  
  
#### Extension properties

##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[alpha](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).alpha\(\))()` Return the alpha component of a color int.  
---|---  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[blue](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).blue\(\))()` Return the blue component of a color int.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[green](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).green\(\))()` Return the green component of a color int.  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[luminance](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).luminance\(\))()` Returns the relative luminance of a color int, assuming sRGB encoding.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[red](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Int\).red\(\))()` Return the red component of a color int.  
  
##### For [kotlin.Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)

[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[alpha](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).alpha\(\))()` Return the alpha component of a color long.  
---|---  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[blue](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).blue\(\))()` Return the blue component of a color long.  
[ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[colorSpace](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).colorSpace\(\))()` Returns the color space encoded in the specified color long.  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[green](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).green\(\))()` Return the green component of a color long.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[isSrgb](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).isSrgb\(\))()` Indicates whether the color is in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace.Named#SRGB) color space.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[isWideGamut](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).isWideGamut\(\))()` Indicates whether the color is in a [wide-gamut](https://developer.android.com/reference/android/graphics/ColorSpace) color space.  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[luminance](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).luminance\(\))()` Returns the relative luminance of a color.  
[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/).[red](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#\(kotlin.Long\).red\(\))()` Return the red component of a color long.  
  
#### Top-level functions

[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) |  `[createBitmap](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#createBitmap\(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config\))(width: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), height: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), config: [Config](https://developer.android.com/reference/android/graphics/Bitmap.Config) = Bitmap.Config.ARGB_8888)` Returns a mutable bitmap with the specified width and height.  
---|---  
[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) |  `[createBitmap](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#createBitmap\(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config,%20kotlin.Boolean,%20android.graphics.ColorSpace\))(width: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), height: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), config: [Config](https://developer.android.com/reference/android/graphics/Bitmap.Config) = Bitmap.Config.ARGB_8888, hasAlpha: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = true, colorSpace: [ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace) = ColorSpace.get(ColorSpace.Named.SRGB))` Returns a mutable bitmap with the specified width and height.  
[Matrix](https://developer.android.com/reference/android/graphics/Matrix) |  `[rotationMatrix](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#rotationMatrix\(kotlin.Float,%20kotlin.Float,%20kotlin.Float\))(degrees: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/), px: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, py: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f)` Creates a rotation matrix, defined by a rotation angle in degrees around the pivot point located at the coordinates (px, py).  
[Matrix](https://developer.android.com/reference/android/graphics/Matrix) |  `[scaleMatrix](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#scaleMatrix\(kotlin.Float,%20kotlin.Float\))(sx: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 1.0f, sy: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 1.0f)` Creates a scale matrix with the scale factor sx and sy respectively on the `x` and `y` axis.  
[Matrix](https://developer.android.com/reference/android/graphics/Matrix) |  `[translationMatrix](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#translationMatrix\(kotlin.Float,%20kotlin.Float\))(tx: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f, ty: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = 0.0f)` Creates a translation matrix with the translation amounts tx and ty respectively on the `x` and `y` axis.  
  
## androidx.core.graphics.drawable

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap)

[Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[toAdaptiveIcon](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(android.graphics.Bitmap\).toAdaptiveIcon\(\))()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) from this adaptive [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).  
---|---  
[BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[toDrawable](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(android.graphics.Bitmap\).toDrawable\(android.content.res.Resources\))(resources: [Resources](https://developer.android.com/reference/android/content/res/Resources))` Create a [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).  
[Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) |  `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).[toIcon](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(android.graphics.Bitmap\).toIcon\(\))()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).  
  
##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color)

[ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable) |  `[Color](https://developer.android.com/reference/android/graphics/Color).[toDrawable](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(android.graphics.Color\).toDrawable\(\))()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable) from this [Color](https://developer.android.com/reference/android/graphics/Color) (via [Color.toArgb](https://developer.android.com/reference/android/graphics/Color#toArgb\(\))).  
---|---  
  
##### For [android.graphics.drawable.Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)

[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) |  `[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable).[toBitmap](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(android.graphics.drawable.Drawable\).toBitmap\(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config\))(@Px width: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = intrinsicWidth, @Px height: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = intrinsicHeight, config: [Config](https://developer.android.com/reference/android/graphics/Bitmap.Config)? = null)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) representation of this [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable).  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable).[updateBounds](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(android.graphics.drawable.Drawable\).updateBounds\(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(@Px left: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = bounds.left, @Px top: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = bounds.top, @Px right: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = bounds.right, @Px bottom: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = bounds.bottom)` Updates this drawable's bounds.  
  
##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri)

[Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) |  `[Uri](https://developer.android.com/reference/android/net/Uri).[toIcon](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(android.net.Uri\).toIcon\(\))()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) from this [Uri](https://developer.android.com/reference/android/net/Uri).  
---|---  
  
##### For [kotlin.ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/)

[Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) |  `[ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/).[toIcon](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(kotlin.ByteArray\).toIcon\(\))()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon) from this [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/).  
---|---  
  
##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

[ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable) |  `[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/).[toDrawable](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#\(kotlin.Int\).toDrawable\(\))()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable) from this color value.  
---|---  
  
## androidx.core.location

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.location.Location](https://developer.android.com/reference/android/location/Location)

operator [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/) |  `[Location](https://developer.android.com/reference/android/location/Location).[component1](https://developer.android.com/reference/kotlin/androidx/core/location/package-summary#\(android.location.Location\).component1\(\))()` Returns the latitude of this [Location](https://developer.android.com/reference/android/location/Location).  
---|---  
operator [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/) |  `[Location](https://developer.android.com/reference/android/location/Location).[component2](https://developer.android.com/reference/kotlin/androidx/core/location/package-summary#\(android.location.Location\).component2\(\))()` Returns the longitude of this [Location](https://developer.android.com/reference/android/location/Location).  
  
## androidx.core.net

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri)

[File](https://developer.android.com/reference/java/io/File) |  `[Uri](https://developer.android.com/reference/android/net/Uri).[toFile](https://developer.android.com/reference/kotlin/androidx/core/net/package-summary#\(android.net.Uri\).toFile\(\))()` Creates a [File](https://developer.android.com/reference/java/io/File) from the given [Uri](https://developer.android.com/reference/android/net/Uri).  
---|---  
  
##### For [java.io.File](https://developer.android.com/reference/java/io/File)

[Uri](https://developer.android.com/reference/android/net/Uri) |  `[File](https://developer.android.com/reference/java/io/File).[toUri](https://developer.android.com/reference/kotlin/androidx/core/net/package-summary#\(java.io.File\).toUri\(\))()` Creates a Uri from the given file.  
---|---  
  
##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

[Uri](https://developer.android.com/reference/android/net/Uri) |  `[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).[toUri](https://developer.android.com/reference/kotlin/androidx/core/net/package-summary#\(kotlin.String\).toUri\(\))()` Creates a Uri from the given encoded URI string.  
---|---  
  
## androidx.core.os

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.os.Handler](https://developer.android.com/reference/android/os/Handler)

[Runnable](https://developer.android.com/reference/java/lang/Runnable) |  `[Handler](https://developer.android.com/reference/android/os/Handler).[postAtTime](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#\(android.os.Handler\).postAtTime\(kotlin.Long,%20kotlin.Any,%20kotlin.Function0\))(uptimeMillis: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), token: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/)? = null, crossinline action: () -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Version of [Handler.postAtTime](https://developer.android.com/reference/android/os/Handler#postAtTime\(java.lang.Runnable,%20long\)) which re-orders the parameters, allowing the action to be placed outside of parentheses.  
---|---  
[Runnable](https://developer.android.com/reference/java/lang/Runnable) |  `[Handler](https://developer.android.com/reference/android/os/Handler).[postDelayed](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#\(android.os.Handler\).postDelayed\(kotlin.Long,%20kotlin.Any,%20kotlin.Function0\))(delayInMillis: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), token: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/)? = null, crossinline action: () -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Version of [Handler.postDelayed](https://developer.android.com/reference/android/os/Handler#postDelayed\(java.lang.Runnable,%20long\)) which re-orders the parameters, allowing the action to be placed outside of parentheses.  
  
#### Top-level functions

[Bundle](https://developer.android.com/reference/android/os/Bundle) |  `[bundleOf](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#bundleOf\(kotlin.Array\))(vararg pairs: [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/)?>)` Returns a new [Bundle](https://developer.android.com/reference/android/os/Bundle) with the given key/value pairs as elements.  
---|---  
[PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle) |  `[persistableBundleOf](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#persistableBundleOf\(kotlin.Array\))(vararg pairs: [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/)?>)` Returns a new [PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle) with the given key/value pairs as elements.  
T |  `[trace](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#trace\(kotlin.String,%20kotlin.Function0\))(sectionName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), block: () -> T)` Wrap the specified block in calls to [Trace.beginSection](https://developer.android.com/reference/android/os/Trace#beginSection\(java.lang.String\)) (with the supplied sectionName) and [Trace.endSection](https://developer.android.com/reference/android/os/Trace#endSection\(\)).  
  
## androidx.core.text

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.text.Spannable](https://developer.android.com/reference/android/text/Spannable)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Spannable](https://developer.android.com/reference/android/text/Spannable).[clearSpans](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.Spannable\).clearSpans\(\))()` Clear all spans from this text.  
---|---  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Spannable](https://developer.android.com/reference/android/text/Spannable).[set](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.Spannable\).set\(kotlin.Int,%20kotlin.Int,%20kotlin.Any\))(start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), end: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), span: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/))` Add span to the range start&hellip;end of the text.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Spannable](https://developer.android.com/reference/android/text/Spannable).[set](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.Spannable\).set\(kotlin.ranges.IntRange,%20kotlin.Any\))(range: [IntRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-int-range/), span: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/))` Add span to the range of the text.  
  
##### For [android.text.SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder)

[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[backgroundColor](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).backgroundColor\(kotlin.Int,%20kotlin.Function1\))(color: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in a [BackgroundColorSpan](https://developer.android.com/reference/android/text/style/BackgroundColorSpan).  
---|---  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[bold](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).bold\(kotlin.Function1\))(builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in a bold [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan).  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[color](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).color\(kotlin.Int,%20kotlin.Function1\))(color: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in a [ForegroundColorSpan](https://developer.android.com/reference/android/text/style/ForegroundColorSpan).  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[inSpans](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).inSpans\(kotlin.Any,%20kotlin.Function1\))(vararg spans: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/), builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in spans.  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[inSpans](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).inSpans\(kotlin.Any,%20kotlin.Function1\))(span: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/), builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in span.  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[italic](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).italic\(kotlin.Function1\))(builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in an italic [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan).  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[scale](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).scale\(kotlin.Float,%20kotlin.Function1\))(proportion: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/), builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in a [RelativeSizeSpan](https://developer.android.com/reference/android/text/style/RelativeSizeSpan).  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[strikeThrough](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).strikeThrough\(kotlin.Function1\))(builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in a [StrikethroughSpan](https://developer.android.com/reference/android/text/style/StrikethroughSpan).  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[subscript](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).subscript\(kotlin.Function1\))(builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in a [SubscriptSpan](https://developer.android.com/reference/android/text/style/SubscriptSpan).  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[superscript](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).superscript\(kotlin.Function1\))(builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in a [SuperscriptSpan](https://developer.android.com/reference/android/text/style/SuperscriptSpan).  
[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) |  `[SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).[underline](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.SpannableStringBuilder\).underline\(kotlin.Function1\))(builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Wrap appended text in builderAction in an [UnderlineSpan](https://developer.android.com/reference/android/text/style/UnderlineSpan).  
  
##### For [android.text.Spanned](https://developer.android.com/reference/android/text/Spanned)

[Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/)<out T> |  `[Spanned](https://developer.android.com/reference/android/text/Spanned).[getSpans](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.Spanned\).getSpans\(kotlin.Int,%20kotlin.Int\))(start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 0, end: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = length)` Get all spans that are instance of T.  
---|---  
[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) |  `[Spanned](https://developer.android.com/reference/android/text/Spanned).[toHtml](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(android.text.Spanned\).toHtml\(kotlin.Int\))(option: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = TO_HTML_PARAGRAPH_LINES_CONSECUTIVE)` Returns a string of HTML from the spans in this [Spanned](https://developer.android.com/reference/android/text/Spanned).  
  
##### For [kotlin.CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/).[isDigitsOnly](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(kotlin.CharSequence\).isDigitsOnly\(\))()` Returns whether the given [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) contains only digits.  
---|---  
[Spannable](https://developer.android.com/reference/android/text/Spannable) |  `[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/).[toSpannable](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(kotlin.CharSequence\).toSpannable\(\))()` Returns a new [Spannable](https://developer.android.com/reference/android/text/Spannable) from [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/), or the source itself if it is already an instance of [SpannableString](https://developer.android.com/reference/android/text/SpannableString).  
[Spanned](https://developer.android.com/reference/android/text/Spanned) |  `[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/).[toSpanned](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(kotlin.CharSequence\).toSpanned\(\))()` Returns a new [Spanned](https://developer.android.com/reference/android/text/Spanned) from [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/), or the source itself if it is already an instance of [SpannedString](https://developer.android.com/reference/android/text/SpannedString).  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/).[trimmedLength](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(kotlin.CharSequence\).trimmedLength\(\))()` Returns the length that the specified [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) would have if spaces and ASCII control characters were trimmed from the start and end, as by [String.trim](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim.html).  
  
##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) |  `[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).[htmlEncode](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(kotlin.String\).htmlEncode\(\))()` Html-encode the string.  
---|---  
[Spanned](https://developer.android.com/reference/android/text/Spanned) |  `[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).[parseAsHtml](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(kotlin.String\).parseAsHtml\(kotlin.Int,%20android.text.Html.ImageGetter,%20android.text.Html.TagHandler\))(flags: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = FROM_HTML_MODE_LEGACY, imageGetter: [ImageGetter](https://developer.android.com/reference/android/text/Html.ImageGetter)? = null, tagHandler: [TagHandler](https://developer.android.com/reference/android/text/Html.TagHandler)? = null)` Returns a [Spanned](https://developer.android.com/reference/android/text/Spanned) from parsing this string as HTML.  
  
#### Extension properties

##### For [java.util.Locale](https://developer.android.com/reference/java/util/Locale)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Locale](https://developer.android.com/reference/java/util/Locale).[layoutDirection](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#\(java.util.Locale\).layoutDirection\(\))()` Returns layout direction for a given locale.  
---|---  
  
#### Top-level functions

[SpannedString](https://developer.android.com/reference/android/text/SpannedString) |  `[buildSpannedString](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#buildSpannedString\(kotlin.Function1\))(builderAction: [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Builds new string by populating a newly created [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder) using the provided builderAction and then converting it to [SpannedString](https://developer.android.com/reference/android/text/SpannedString).  
---|---  
  
## androidx.core.transition

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.transition.Transition](https://developer.android.com/reference/android/transition/Transition)

[TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener) |  `[Transition](https://developer.android.com/reference/android/transition/Transition).[addListener](https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#\(android.transition.Transition\).addListener\(kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1\))(crossinline onEnd: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onStart: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onCancel: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onResume: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, crossinline onPause: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {})` Add a listener to this Transition using the provided actions.  
---|---  
[TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener) |  `[Transition](https://developer.android.com/reference/android/transition/Transition).[doOnCancel](https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#\(android.transition.Transition\).doOnCancel\(kotlin.Function1\))(crossinline action: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when this transition has been cancelled.  
[TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener) |  `[Transition](https://developer.android.com/reference/android/transition/Transition).[doOnEnd](https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#\(android.transition.Transition\).doOnEnd\(kotlin.Function1\))(crossinline action: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when this transition has ended.  
[TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener) |  `[Transition](https://developer.android.com/reference/android/transition/Transition).[doOnPause](https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#\(android.transition.Transition\).doOnPause\(kotlin.Function1\))(crossinline action: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when this transition has been paused.  
[TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener) |  `[Transition](https://developer.android.com/reference/android/transition/Transition).[doOnResume](https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#\(android.transition.Transition\).doOnResume\(kotlin.Function1\))(crossinline action: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when this transition has resumed after a pause.  
[TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener) |  `[Transition](https://developer.android.com/reference/android/transition/Transition).[doOnStart](https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#\(android.transition.Transition\).doOnStart\(kotlin.Function1\))(crossinline action: (transition: [Transition](https://developer.android.com/reference/android/transition/Transition)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when this transition has started.  
  
## androidx.core.util

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.util.AtomicFile](https://developer.android.com/reference/android/util/AtomicFile)

[ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/) |  `[AtomicFile](https://developer.android.com/reference/android/util/AtomicFile).[readBytes](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.AtomicFile\).readBytes\(\))()` Gets the entire content of this file as a byte array.  
---|---  
[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) |  `[AtomicFile](https://developer.android.com/reference/android/util/AtomicFile).[readText](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.AtomicFile\).readText\(java.nio.charset.Charset\))(charset: [Charset](https://developer.android.com/reference/java/nio/charset/Charset) = Charsets.UTF_8)` Gets the entire content of this file as a String using UTF-8 or specified charset.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[AtomicFile](https://developer.android.com/reference/android/util/AtomicFile).[tryWrite](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.AtomicFile\).tryWrite\(kotlin.Function1\))(block: (out: [FileOutputStream](https://developer.android.com/reference/java/io/FileOutputStream)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Perform the write operations inside block on this file.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[AtomicFile](https://developer.android.com/reference/android/util/AtomicFile).[writeBytes](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.AtomicFile\).writeBytes\(kotlin.ByteArray\))(array: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/))` Sets the content of this file as an array of bytes.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[AtomicFile](https://developer.android.com/reference/android/util/AtomicFile).[writeText](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.AtomicFile\).writeText\(kotlin.String,%20java.nio.charset.Charset\))(text: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), charset: [Charset](https://developer.android.com/reference/java/nio/charset/Charset) = Charsets.UTF_8)` Sets the content of this file as text encoded using UTF-8 or specified charset.  
  
##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[contains](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).contains\(kotlin.Long\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Returns true if the collection contains key.  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[containsKey](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).containsKey\(kotlin.Long\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Returns true if the collection contains key.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[containsValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).containsValue\(kotlin.Any\))(value: T)` Returns true if the collection contains value.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[forEach](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).forEach\(kotlin.Function2\))(action: (key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), value: T) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action for each key/value entry.  
T |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[getOrDefault](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).getOrDefault\(kotlin.Long,kotlin.Any\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), defaultValue: T)` Return the value corresponding to key, or defaultValue when not present.  
T |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[getOrElse](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).getOrElse\(kotlin.Long,%20kotlin.Function0\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), defaultValue: () -> T)` Return the value corresponding to key, or from defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[isEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).isEmpty\(\))()` Return true when the collection contains no elements.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).isNotEmpty\(\))()` Return true when the collection contains elements.  
[LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[keyIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).keyIterator\(\))()` Return an iterator over the collection's keys.  
operator [LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T> |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[plus](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).plus\(android.util.LongSparseArray\))(other: [LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>)` Creates a new collection by adding or replacing entries from other.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[putAll](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).putAll\(android.util.LongSparseArray\))(other: [LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>)` Update this collection by adding or replacing entries from other.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[remove](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).remove\(kotlin.Long,kotlin.Any\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), value: T)` Removes the entry for key only if it is mapped to value.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[set](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).set\(kotlin.Long,kotlin.Any\))(key: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), value: T)` Allows the use of the index operator for storing values in the collection.  
[Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[valueIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).valueIterator\(\))()` Return an iterator over the collection's values.  
  
##### For [android.util.Pair](https://developer.android.com/reference/android/util/Pair)

operator F |  `[Pair](https://developer.android.com/reference/android/util/Pair)<F, S>.[component1](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Pair\).component1\(\))()` Returns the first component of the pair.  
---|---  
operator S |  `[Pair](https://developer.android.com/reference/android/util/Pair)<F, S>.[component2](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Pair\).component2\(\))()` Returns the second component of the pair.  
[Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<F, S> |  `[Pair](https://developer.android.com/reference/android/util/Pair)<F, S>.[toKotlinPair](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Pair\).toKotlinPair\(\))()` Returns this [Pair](https://developer.android.com/reference/android/util/Pair) as a [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/).  
  
##### For [android.util.Range](https://developer.android.com/reference/android/util/Range)

infix [Range](https://developer.android.com/reference/android/util/Range)<T> |  `[Range](https://developer.android.com/reference/android/util/Range)<T>.[and](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Range\).and\(android.util.Range\))(other: [Range](https://developer.android.com/reference/android/util/Range)<T>)` Return the intersection of this range and other.  
---|---  
operator [Range](https://developer.android.com/reference/android/util/Range)<T> |  `[Range](https://developer.android.com/reference/android/util/Range)<T>.[plus](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Range\).plus\(kotlin.Comparable\))(value: T)` Return the smallest range that includes this and value.  
operator [Range](https://developer.android.com/reference/android/util/Range)<T> |  `[Range](https://developer.android.com/reference/android/util/Range)<T>.[plus](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Range\).plus\(android.util.Range\))(other: [Range](https://developer.android.com/reference/android/util/Range)<T>)` Return the smallest range that includes this and other.  
[ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/)<T> |  `[Range](https://developer.android.com/reference/android/util/Range)<T>.[toClosedRange](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Range\).toClosedRange\(\))()` Returns this [Range](https://developer.android.com/reference/android/util/Range) as a [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/).  
  
##### For [android.util.Size](https://developer.android.com/reference/android/util/Size)

operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Size](https://developer.android.com/reference/android/util/Size).[component1](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Size\).component1\(\))()` Returns "width", the first component of this [Size](https://developer.android.com/reference/android/util/Size).  
---|---  
operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Size](https://developer.android.com/reference/android/util/Size).[component2](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.Size\).component2\(\))()` Returns "height", the second component of this [Size](https://developer.android.com/reference/android/util/Size).  
  
##### For [android.util.SizeF](https://developer.android.com/reference/android/util/SizeF)

operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[SizeF](https://developer.android.com/reference/android/util/SizeF).[component1](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SizeF\).component1\(\))()` Returns "width", the first component of this [SizeF](https://developer.android.com/reference/android/util/SizeF).  
---|---  
operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) |  `[SizeF](https://developer.android.com/reference/android/util/SizeF).[component2](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SizeF\).component2\(\))()` Returns "height", the second component of this [SizeF](https://developer.android.com/reference/android/util/SizeF).  
  
##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[contains](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).contains\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[containsKey](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).containsKey\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[containsValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).containsValue\(kotlin.Any\))(value: T)` Returns true if the collection contains value.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[forEach](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).forEach\(kotlin.Function2\))(action: (key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: T) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action for each key/value entry.  
T |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[getOrDefault](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).getOrDefault\(kotlin.Int,kotlin.Any\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: T)` Return the value corresponding to key, or defaultValue when not present.  
T |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[getOrElse](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).getOrElse\(kotlin.Int,%20kotlin.Function0\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: () -> T)` Return the value corresponding to key, or from defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[isEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).isEmpty\(\))()` Return true when the collection contains no elements.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).isNotEmpty\(\))()` Return true when the collection contains elements.  
[IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[keyIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).keyIterator\(\))()` Return an iterator over the collection's keys.  
operator [SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T> |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[plus](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).plus\(android.util.SparseArray\))(other: [SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>)` Creates a new collection by adding or replacing entries from other.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[putAll](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).putAll\(android.util.SparseArray\))(other: [SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>)` Update this collection by adding or replacing entries from other.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[remove](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).remove\(kotlin.Int,kotlin.Any\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: T)` Removes the entry for key only if it is mapped to value.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[set](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).set\(kotlin.Int,kotlin.Any\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: T)` Allows the use of the index operator for storing values in the collection.  
[Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[valueIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).valueIterator\(\))()` Return an iterator over the collection's values.  
  
##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[contains](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).contains\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[containsKey](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).containsKey\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[containsValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).containsValue\(kotlin.Boolean\))(value: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/))` Returns true if the collection contains value.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[forEach](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).forEach\(kotlin.Function2\))(action: (key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action for each key/value entry.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[getOrDefault](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).getOrDefault\(kotlin.Int,%20kotlin.Boolean\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/))` Return the value corresponding to key, or defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[getOrElse](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).getOrElse\(kotlin.Int,%20kotlin.Function0\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: () -> [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/))` Return the value corresponding to key, or from defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[isEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).isEmpty\(\))()` Return true when the collection contains no elements.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).isNotEmpty\(\))()` Return true when the collection contains elements.  
[IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[keyIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).keyIterator\(\))()` Return an iterator over the collection's keys.  
operator [SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[plus](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).plus\(android.util.SparseBooleanArray\))(other: [SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray))` Creates a new collection by adding or replacing entries from other.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[putAll](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).putAll\(android.util.SparseBooleanArray\))(other: [SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray))` Update this collection by adding or replacing entries from other.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[remove](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).remove\(kotlin.Int,%20kotlin.Boolean\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/))` Removes the entry for key only if it is mapped to value.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[set](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).set\(kotlin.Int,%20kotlin.Boolean\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/))` Allows the use of the index operator for storing values in the collection.  
[BooleanIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-boolean-iterator/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[valueIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).valueIterator\(\))()` Return an iterator over the collection's values.  
  
##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[contains](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).contains\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[containsKey](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).containsKey\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[containsValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).containsValue\(kotlin.Int\))(value: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains value.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[forEach](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).forEach\(kotlin.Function2\))(action: (key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action for each key/value entry.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[getOrDefault](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).getOrDefault\(kotlin.Int,%20kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Return the value corresponding to key, or defaultValue when not present.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[getOrElse](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).getOrElse\(kotlin.Int,%20kotlin.Function0\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: () -> [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Return the value corresponding to key, or from defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[isEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).isEmpty\(\))()` Return true when the collection contains no elements.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).isNotEmpty\(\))()` Return true when the collection contains elements.  
[IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[keyIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).keyIterator\(\))()` Return an iterator over the collection's keys.  
operator [SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[plus](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).plus\(android.util.SparseIntArray\))(other: [SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray))` Creates a new collection by adding or replacing entries from other.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[putAll](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).putAll\(android.util.SparseIntArray\))(other: [SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray))` Update this collection by adding or replacing entries from other.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[remove](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).remove\(kotlin.Int,%20kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Removes the entry for key only if it is mapped to value.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[set](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).set\(kotlin.Int,%20kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Allows the use of the index operator for storing values in the collection.  
[IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[valueIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).valueIterator\(\))()` Return an iterator over the collection's values.  
  
##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[contains](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).contains\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[containsKey](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).containsKey\(kotlin.Int\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns true if the collection contains key.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[containsValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).containsValue\(kotlin.Long\))(value: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Returns true if the collection contains value.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[forEach](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).forEach\(kotlin.Function2\))(action: (key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action for each key/value entry.  
[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[getOrDefault](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).getOrDefault\(kotlin.Int,%20kotlin.Long\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Return the value corresponding to key, or defaultValue when not present.  
[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[getOrElse](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).getOrElse\(kotlin.Int,%20kotlin.Function0\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), defaultValue: () -> [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Return the value corresponding to key, or from defaultValue when not present.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[isEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).isEmpty\(\))()` Return true when the collection contains no elements.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).isNotEmpty\(\))()` Return true when the collection contains elements.  
[IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[keyIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).keyIterator\(\))()` Return an iterator over the collection's keys.  
operator [SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[plus](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).plus\(android.util.SparseLongArray\))(other: [SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray))` Creates a new collection by adding or replacing entries from other.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[putAll](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).putAll\(android.util.SparseLongArray\))(other: [SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray))` Update this collection by adding or replacing entries from other.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[remove](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).remove\(kotlin.Int,%20kotlin.Long\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Removes the entry for key only if it is set to value.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[set](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).set\(kotlin.Int,%20kotlin.Long\))(key: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), value: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))` Allows the use of the index operator for storing values in the collection.  
[LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[valueIterator](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).valueIterator\(\))()` Return an iterator over the collection's values.  
  
##### For [kotlin.Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/)

[Half](https://developer.android.com/reference/android/util/Half) |  `[Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/).[toHalf](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(kotlin.Double\).toHalf\(\))()` Returns a [Half](https://developer.android.com/reference/android/util/Half) instance representing given [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/).  
---|---  
  
##### For [kotlin.Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)

[Half](https://developer.android.com/reference/android/util/Half) |  `[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/).[toHalf](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(kotlin.Float\).toHalf\(\))()` Returns a [Half](https://developer.android.com/reference/android/util/Half) instance representing given [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/).  
---|---  
  
##### For [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)

[Pair](https://developer.android.com/reference/android/util/Pair)<F, S> |  `[Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<F, S>.[toAndroidPair](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(kotlin.Pair\).toAndroidPair\(\))()` Returns this [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/) as an Android [Pair](https://developer.android.com/reference/android/util/Pair).  
---|---  
  
##### For [kotlin.Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/)

[Half](https://developer.android.com/reference/android/util/Half) |  `[Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/).[toHalf](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(kotlin.Short\).toHalf\(\))()` Returns a [Half](https://developer.android.com/reference/android/util/Half) instance representing given [Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/).  
---|---  
  
##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

[Half](https://developer.android.com/reference/android/util/Half) |  `[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).[toHalf](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(kotlin.String\).toHalf\(\))()` Returns a [Half](https://developer.android.com/reference/android/util/Half) instance representing given [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).  
---|---  
  
##### For [kotlin.ranges.ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/)

[Range](https://developer.android.com/reference/android/util/Range)<T> |  `[ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/)<T>.[toRange](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(kotlin.ranges.ClosedRange\).toRange\(\))()` Returns this [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/) as a [Range](https://developer.android.com/reference/android/util/Range).  
---|---  
  
#### Extension properties

##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray)<T>.[size](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.LongSparseArray\).size\(\))()` Returns the number of key/value pairs in the collection.  
---|---  
  
##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SparseArray](https://developer.android.com/reference/android/util/SparseArray)<T>.[size](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseArray\).size\(\))()` Returns the number of key/value pairs in the collection.  
---|---  
  
##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray).[size](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseBooleanArray\).size\(\))()` Returns the number of key/value pairs in the collection.  
---|---  
  
##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray).[size](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseIntArray\).size\(\))()` Returns the number of key/value pairs in the collection.  
---|---  
  
##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray).[size](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(android.util.SparseLongArray\).size\(\))()` Returns the number of key/value entries in the collection.  
---|---  
  
#### Top-level functions

[LruCache](https://developer.android.com/reference/android/util/LruCache)<K, V> |  `[lruCache](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#lruCache\(kotlin.Int,%20kotlin.Function2,%20kotlin.Function1,%20kotlin.Function4\))(maxSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), crossinline sizeOf: (key: K, value: V) -> [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/), key: K, oldValue: V, newValue: V?) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = { _, _, _, _ -> })` Creates an [LruCache](https://developer.android.com/reference/android/util/LruCache) with the given parameters.  
---|---  
infix [Range](https://developer.android.com/reference/android/util/Range)<T> |  `T.[rangeTo](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#\(kotlin.Comparable\).rangeTo\(kotlin.Comparable\))(that: T)` Creates a range from this [Comparable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-comparable/) value to that.  
  
## androidx.core.view

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[contains](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).contains\(android.view.MenuItem\))(item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem))` Returns `true` if item is found in this menu.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[forEach](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).forEach\(kotlin.Function1\))(action: (item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action on each item in this menu.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[forEachIndexed](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).forEachIndexed\(kotlin.Function2\))(action: (index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action on each item in this menu, providing its sequential index.  
operator [MenuItem](https://developer.android.com/reference/android/view/MenuItem) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[get](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).get\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the menu at index.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[isEmpty](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).isEmpty\(\))()` Returns true if this menu contains no items.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).isNotEmpty\(\))()` Returns true if this menu contains one or more items.  
operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)<[MenuItem](https://developer.android.com/reference/android/view/MenuItem)> |  `[Menu](https://developer.android.com/reference/android/view/Menu).[iterator](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).iterator\(\))()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the items in this menu.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[minusAssign](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).minusAssign\(android.view.MenuItem\))(item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem))` Removes item from this menu.  
  
##### For [android.view.View](https://developer.android.com/reference/android/view/View)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[doOnAttach](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).doOnAttach\(kotlin.Function1\))(crossinline action: (view: [View](https://developer.android.com/reference/android/view/View)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action when this view is attached to a window.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[doOnDetach](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).doOnDetach\(kotlin.Function1\))(crossinline action: (view: [View](https://developer.android.com/reference/android/view/View)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action when this view is detached from a window.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[doOnLayout](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).doOnLayout\(kotlin.Function1\))(crossinline action: (view: [View](https://developer.android.com/reference/android/view/View)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action when this view is laid out.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[doOnNextLayout](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).doOnNextLayout\(kotlin.Function1\))(crossinline action: (view: [View](https://developer.android.com/reference/android/view/View)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action when this view is next laid out.  
[OneShotPreDrawListener](https://developer.android.com/reference/kotlin/androidx/core/view/OneShotPreDrawListener) |  `[View](https://developer.android.com/reference/android/view/View).[doOnPreDraw](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).doOnPreDraw\(kotlin.Function1\))(crossinline action: (view: [View](https://developer.android.com/reference/android/view/View)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action when the view tree is about to be drawn.  
[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) |  `[View](https://developer.android.com/reference/android/view/View).[drawToBitmap](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).drawToBitmap\(android.graphics.Bitmap.Config\))(config: [Config](https://developer.android.com/reference/android/graphics/Bitmap.Config) = Bitmap.Config.ARGB_8888)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) representation of this [View](https://developer.android.com/reference/android/view/View).  
[Runnable](https://developer.android.com/reference/java/lang/Runnable) |  `[View](https://developer.android.com/reference/android/view/View).[postDelayed](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).postDelayed\(kotlin.Long,%20kotlin.Function0\))(delayInMillis: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), crossinline action: () -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Version of [View.postDelayed](https://developer.android.com/reference/android/view/View#postDelayed\(java.lang.Runnable,%20long\)) which re-orders the parameters, allowing the action to be placed outside of parentheses.  
[Runnable](https://developer.android.com/reference/java/lang/Runnable) |  `[View](https://developer.android.com/reference/android/view/View).[postOnAnimationDelayed](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).postOnAnimationDelayed\(kotlin.Long,%20kotlin.Function0\))(delayInMillis: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), crossinline action: () -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Version of [View.postOnAnimationDelayed](https://developer.android.com/reference/android/view/View#postOnAnimationDelayed\(java.lang.Runnable,%20long\)) which re-orders the parameters, allowing the action to be placed outside of parentheses.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[setPadding](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).setPadding\(kotlin.Int\))(@Px size: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Sets the view's padding.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[updateLayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).updateLayoutParams\(kotlin.Function1\))(block: [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Executes block with the View's layoutParams and reassigns the layoutParams with the updated version.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[updateLayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).updateLayoutParams\(kotlin.Function1\))(block: T.() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Executes block with a typed version of the View's layoutParams and reassigns the layoutParams with the updated version.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[updatePadding](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).updatePadding\(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(@Px left: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingLeft, @Px top: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingTop, @Px right: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingRight, @Px bottom: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingBottom)` Updates this view's padding.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[View](https://developer.android.com/reference/android/view/View).[updatePaddingRelative](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).updatePaddingRelative\(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(@Px start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingStart, @Px top: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingTop, @Px end: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingEnd, @Px bottom: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = paddingBottom)` Updates this view's relative padding.  
  
##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[contains](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).contains\(android.view.View\))(view: [View](https://developer.android.com/reference/android/view/View))` Returns `true` if view is found in this view group.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[forEach](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).forEach\(kotlin.Function1\))(action: (view: [View](https://developer.android.com/reference/android/view/View)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action on each view in this view group.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[forEachIndexed](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).forEachIndexed\(kotlin.Function2\))(action: (index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), view: [View](https://developer.android.com/reference/android/view/View)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action on each view in this view group, providing its sequential index.  
operator [View](https://developer.android.com/reference/android/view/View) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[get](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).get\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the view at index.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[isEmpty](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).isEmpty\(\))()` Returns true if this view group contains no views.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).isNotEmpty\(\))()` Returns true if this view group contains one or more views.  
operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)<[View](https://developer.android.com/reference/android/view/View)> |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[iterator](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).iterator\(\))()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the views in this view group.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[minusAssign](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).minusAssign\(android.view.View\))(view: [View](https://developer.android.com/reference/android/view/View))` Removes view from this view group.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[plusAssign](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).plusAssign\(android.view.View\))(view: [View](https://developer.android.com/reference/android/view/View))` Adds view to this view group.  
  
##### For [android.view.ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams).[setMargins](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup.MarginLayoutParams\).setMargins\(kotlin.Int\))(@Px size: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Sets the margins in the ViewGroup's MarginLayoutParams.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams).[updateMargins](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup.MarginLayoutParams\).updateMargins\(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(@Px left: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = leftMargin, @Px top: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = topMargin, @Px right: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = rightMargin, @Px bottom: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = bottomMargin)` Updates the margins in the [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup)'s [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams).  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams).[updateMarginsRelative](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup.MarginLayoutParams\).updateMarginsRelative\(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(@Px start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = marginStart, @Px top: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = topMargin, @Px end: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = marginEnd, @Px bottom: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = bottomMargin)` Updates the relative margins in the ViewGroup's MarginLayoutParams.  
  
#### Extension properties

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu)

[Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)<[MenuItem](https://developer.android.com/reference/android/view/MenuItem)> |  `[Menu](https://developer.android.com/reference/android/view/Menu).[children](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).children\(\))()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the items in this menu.  
---|---  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[Menu](https://developer.android.com/reference/android/view/Menu).[size](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.Menu\).size\(\))()` Returns the number of items in this menu.  
  
##### For [android.view.View](https://developer.android.com/reference/android/view/View)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[View](https://developer.android.com/reference/android/view/View).[isGone](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).isGone\(\))()` Returns true when this view's visibility is [View.GONE](https://developer.android.com/reference/android/view/View#GONE), false otherwise.  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[View](https://developer.android.com/reference/android/view/View).[isInvisible](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).isInvisible\(\))()` Returns true when this view's visibility is [View.INVISIBLE](https://developer.android.com/reference/android/view/View#INVISIBLE), false otherwise.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[View](https://developer.android.com/reference/android/view/View).[isVisible](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).isVisible\(\))()` Returns true when this view's visibility is [View.VISIBLE](https://developer.android.com/reference/android/view/View#VISIBLE), false otherwise.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[View](https://developer.android.com/reference/android/view/View).[marginBottom](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).marginBottom\(\))()` Returns the bottom margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[View](https://developer.android.com/reference/android/view/View).[marginEnd](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).marginEnd\(\))()` Returns the end margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[View](https://developer.android.com/reference/android/view/View).[marginLeft](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).marginLeft\(\))()` Returns the left margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[View](https://developer.android.com/reference/android/view/View).[marginRight](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).marginRight\(\))()` Returns the right margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[View](https://developer.android.com/reference/android/view/View).[marginStart](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).marginStart\(\))()` Returns the start margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[View](https://developer.android.com/reference/android/view/View).[marginTop](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.View\).marginTop\(\))()` Returns the top margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0.  
  
##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup)

[Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)<[View](https://developer.android.com/reference/android/view/View)> |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[children](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).children\(\))()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the child views in this view group.  
---|---  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup).[size](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#\(android.view.ViewGroup\).size\(\))()` Returns the number of views in this view group.  
  
## androidx.core.widget

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-ktx:1.19.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-ktx:1.19.1")
    }

#### Extension functions

##### For [android.widget.TextView](https://developer.android.com/reference/android/widget/TextView)

[TextWatcher](https://developer.android.com/reference/android/text/TextWatcher) |  `[TextView](https://developer.android.com/reference/android/widget/TextView).[addTextChangedListener](https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#\(android.widget.TextView\).addTextChangedListener\(kotlin.Function4,%20kotlin.Function4,%20kotlin.Function1\))(crossinline beforeTextChanged: (text: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)?, start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), count: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), after: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = { _, _, _, _ -> }, crossinline onTextChanged: (text: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)?, start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), count: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), after: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = { _, _, _, _ -> }, crossinline afterTextChanged: (text: [Editable](https://developer.android.com/reference/android/text/Editable)?) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {})` Add a text changed listener to this TextView using the provided actions  
---|---  
[TextWatcher](https://developer.android.com/reference/android/text/TextWatcher) |  `[TextView](https://developer.android.com/reference/android/widget/TextView).[doAfterTextChanged](https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#\(android.widget.TextView\).doAfterTextChanged\(kotlin.Function1\))(crossinline action: (text: [Editable](https://developer.android.com/reference/android/text/Editable)?) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked after the text changed.  
[TextWatcher](https://developer.android.com/reference/android/text/TextWatcher) |  `[TextView](https://developer.android.com/reference/android/widget/TextView).[doBeforeTextChanged](https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#\(android.widget.TextView\).doBeforeTextChanged\(kotlin.Function4\))(crossinline action: (text: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)?, start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), count: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), after: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked before the text changed.  
[TextWatcher](https://developer.android.com/reference/android/text/TextWatcher) |  `[TextView](https://developer.android.com/reference/android/widget/TextView).[doOnTextChanged](https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#\(android.widget.TextView\).doOnTextChanged\(kotlin.Function4\))(crossinline action: (text: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)?, start: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), count: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), after: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Add an action which will be invoked when the text is changing.  
  
## androidx.dynamicanimation.animation

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.dynamicanimation:dynamicanimation-ktx:"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.dynamicanimation:dynamicanimation-ktx:")
    }

#### Extension functions

##### For [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation)

[SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) |  `[SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation).[withSpringForceProperties](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/package-summary#\(androidx.dynamicanimation.animation.SpringAnimation\).withSpringForceProperties\(kotlin.Function1\))(func: [SpringForce](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringForce).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Updates or applies spring force properties like [SpringForce.mDampingRatio](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringForce#getDampingRatio\(\)), [SpringForce.mFinalPosition](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringForce#getFinalPosition\(\)) and stiffness on SpringAnimation.  
---|---  
  
#### Top-level functions

[FlingAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) |  `[flingAnimationOf](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/package-summary#flingAnimationOf\(kotlin.Function1,%20kotlin.Function0\))(setter: ([Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/), getter: () -> [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/))` Creates [FlingAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) for a property that can be accessed via the provided setter and getter.  
---|---  
[SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) |  `[springAnimationOf](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/package-summary#springAnimationOf\(kotlin.Function1,%20kotlin.Function0,%20kotlin.Float\))(setter: ([Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/), getter: () -> [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/), finalPosition: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) = Float.NaN)` Creates [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) for a property that can be accessed via the provided setter and getter.  
  
## androidx.fragment.app

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.fragment:fragment-ktx:1.9.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.fragment:fragment-ktx:1.9.1")
    }

#### Extension functions

##### For [android.view.View](https://developer.android.com/reference/android/view/View)

F |  `[View](https://developer.android.com/reference/android/view/View).[findFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(android.view.View\).findFragment\(\))()` Find a [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) associated with a [View](https://developer.android.com/reference/android/view/View).  
---|---  
  
##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[activityViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).activityViewModels\(kotlin.Function0,kotlin.Function0\))(noinline factoryProducer: () -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) = null)` Returns a property delegate to access parent activity's [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel), if factoryProducer is specified then [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) first time.  
---|---  
[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[createViewModelLazy](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).createViewModelLazy\(kotlin.reflect.KClass,kotlin.Function0,kotlin.Function0,kotlin.Function0\))(viewModelClass: [KClass](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-class/)<VM>, storeProducer: () -> [ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore), factoryProducer: () -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) = null)` Helper method for creation of [ViewModelLazy](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelLazy), that resolves `null` passed as factoryProducer to default factory.  
[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[viewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).viewModels\(kotlin.Function0,kotlin.Function0,kotlin.Function0\))(noinline ownerProducer: () -> [ViewModelStoreOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner) = { this }, noinline factoryProducer: () -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) = null)` Returns a property delegate to access [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) by **default** scoped to this [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment):  
  
##### For [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction)

[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) |  `[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction).[add](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.FragmentTransaction\).add\(kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(@IdRes containerViewId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), tag: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)? = null, args: [Bundle](https://developer.android.com/reference/android/os/Bundle)? = null)` Add a fragment to the associated [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager), inflating the Fragment's view into the container view specified by containerViewId, to later retrieve via [FragmentManager.findFragmentById](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#findFragmentById\(int\)).  
---|---  
[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) |  `[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction).[add](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.FragmentTransaction\).add\(kotlin.String,%20android.os.Bundle\))(tag: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), args: [Bundle](https://developer.android.com/reference/android/os/Bundle)? = null)` Add a fragment to the associated [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager) without adding the Fragment to any container view.  
[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) |  `[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction).[replace](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.FragmentTransaction\).replace\(kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(@IdRes containerViewId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), tag: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)? = null, args: [Bundle](https://developer.android.com/reference/android/os/Bundle)? = null)` Replace an existing fragment that was added to a container.  
  
##### For [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager).[commit](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.FragmentManager\).commit\(kotlin.Boolean,%20kotlin.Function1\))(allowStateLoss: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = false, body: [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Run body in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager).[commitNow](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.FragmentManager\).commitNow\(kotlin.Boolean,%20kotlin.Function1\))(allowStateLoss: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = false, body: [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Run body in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager).[transaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.FragmentManager\).transaction\(kotlin.Boolean,%20kotlin.Boolean,%20kotlin.Function1\))(now: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = false, allowStateLoss: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = false, body: [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Run body in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception.  
  
## androidx.fragment.app.testing

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.fragment:fragment-testing:1.9.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.fragment:fragment-testing:1.9.1")
    }

#### Top-level functions

[FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> |  `[launchFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragment\(android.os.Bundle,kotlin.Int,androidx.lifecycle.Lifecycle.State,androidx.fragment.app.FragmentFactory\))(fragmentArgs: [Bundle](https://developer.android.com/reference/android/os/Bundle)? = null, @StyleRes themeResId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: [FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory)? = null)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) using given [FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory) and waits for it to reach a resumed state.  
---|---  
[FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> |  `[launchFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragment\(android.os.Bundle,kotlin.Int,androidx.lifecycle.Lifecycle.State,kotlin.Function0\))(fragmentArgs: [Bundle](https://developer.android.com/reference/android/os/Bundle)? = null, @StyleRes themeResId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) using instantiate to create the Fragment and waits for it to reach a resumed state.  
[FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> |  `[launchFragmentInContainer](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragmentInContainer\(android.os.Bundle,kotlin.Int,androidx.lifecycle.Lifecycle.State,androidx.fragment.app.FragmentFactory\))(fragmentArgs: [Bundle](https://developer.android.com/reference/android/os/Bundle)? = null, @StyleRes themeResId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: [FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory)? = null)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) and waits for it to reach a resumed state.  
[FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> |  `[launchFragmentInContainer](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragmentInContainer\(android.os.Bundle,kotlin.Int,androidx.lifecycle.Lifecycle.State,kotlin.Function0\))(fragmentArgs: [Bundle](https://developer.android.com/reference/android/os/Bundle)? = null, @StyleRes themeResId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) using instantiate to create the Fragment and waits for it to reach a resumed state.  
  
## androidx.lifecycle

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.lifecycle:lifecycle-livedata-core-ktx:2.11.0"
        implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.11.0"
        implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:2.11.0"
        implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.11.0"
        implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.11.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.lifecycle:lifecycle-livedata-core-ktx:2.11.0")
        implementation("androidx.lifecycle:lifecycle-livedata-ktx:2.11.0")
        implementation("androidx.lifecycle:lifecycle-reactivestreams-ktx:2.11.0")
        implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.11.0")
        implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.11.0")
    }

#### Extension functions

##### For [kotlinx.coroutines.flow.Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)

[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T> |  `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)<T>.[asLiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(kotlinx.coroutines.flow.Flow\).asLiveData\(kotlin.coroutines.CoroutineContext,%20kotlin.Long\))(context: [CoroutineContext](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/-coroutine-context/) = EmptyCoroutineContext, timeoutInMs: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) = DEFAULT_TIMEOUT)` Creates a LiveData that has values collected from the origin [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/).  
---|---  
[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T> |  `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)<T>.[asLiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(kotlinx.coroutines.flow.Flow\).asLiveData\(java.time.Duration,kotlin.coroutines.CoroutineContext\))(context: [CoroutineContext](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/-coroutine-context/) = EmptyCoroutineContext, timeout: [Duration](https://developer.android.com/reference/java/time/Duration))` Creates a LiveData that has values collected from the origin [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/).  
  
##### For [org.reactivestreams.Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(org.reactivestreams.Publisher\).toLiveData\(\))

[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T> |  `Publisher<T>.[toLiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(org.reactivestreams.Publisher\).toLiveData\(\))()` Creates an observable [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) stream from a ReactiveStreams [Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(org.reactivestreams.Publisher\).toLiveData\(\)).  
---|---  
  
##### For [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)

[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)<T> |  `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T>.[asFlow](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LiveData\).asFlow\(\))()` Creates a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) containing values dispatched by originating [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData): at the start a flow collector receives the latest value held by LiveData and then observes LiveData updates.  
---|---  
[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<X> |  `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<X>.[distinctUntilChanged](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LiveData\).distinctUntilChanged\(\))()` Creates a new [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) object does not emit a value until the source `this` LiveData value has been changed.  
[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<Y> |  `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<X>.[map](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LiveData\).map\(kotlin.Function1\))(crossinline transform: (X) -> Y)` Returns a [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) mapped from `this` LiveData by applying transform to each value set on `this` LiveData.  
[Observer](https://developer.android.com/reference/kotlin/androidx/lifecycle/Observer)<T> |  `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T>.[observe](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LiveData\).observe\(androidx.lifecycle.LifecycleOwner,%20kotlin.Function1\))(owner: [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner), crossinline onChanged: (T) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Adds the given onChanged lambda as an observer within the lifespan of the given owner and returns a reference to observer.  
[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<Y> |  `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<X>.[switchMap](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LiveData\).switchMap\(kotlin.Function1\))(crossinline transform: (X) -> [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<Y>)` Returns a [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) mapped from the input `this` `LiveData` by applying transform to each value set on `this`.  
Publisher<T> |  `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T>.[toPublisher](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LiveData\).toPublisher\(androidx.lifecycle.LifecycleOwner\))(lifecycle: [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner))` Adapts the given [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) stream to a ReactiveStreams [Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(org.reactivestreams.Publisher\).toLiveData\(\)).  
  
##### For [ViewModelProvider](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider)

VM |  `[ViewModelProvider](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider).[get](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.ViewModelProvider\).get\(\))()` Returns an existing ViewModel or creates a new one in the scope (usually, a fragment or an activity), associated with this `ViewModelProvider`.  
---|---  
  
##### For [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)

suspend T |  `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner).[whenCreated](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LifecycleOwner\).whenCreated\(kotlin.coroutines.SuspendFunction1\))(block: suspend [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/).() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#CREATED) state.  
---|---  
suspend T |  `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner).[whenResumed](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LifecycleOwner\).whenResumed\(kotlin.coroutines.SuspendFunction1\))(block: suspend [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/).() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#RESUMED) state.  
suspend T |  `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner).[whenStarted](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LifecycleOwner\).whenStarted\(kotlin.coroutines.SuspendFunction1\))(block: suspend [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/).() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#STARTED) state.  
  
##### For [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)

suspend T |  `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle).[whenCreated](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.Lifecycle\).whenCreated\(kotlin.coroutines.SuspendFunction1\))(block: suspend [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/).() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#CREATED) state.  
---|---  
suspend T |  `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle).[whenResumed](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.Lifecycle\).whenResumed\(kotlin.coroutines.SuspendFunction1\))(block: suspend [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/).() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#RESUMED) state.  
suspend T |  `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle).[whenStarted](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.Lifecycle\).whenStarted\(kotlin.coroutines.SuspendFunction1\))(block: suspend [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/).() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#STARTED) state.  
suspend T |  `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle).[whenStateAtLeast](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.Lifecycle\).whenStateAtLeast\(androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1\))(minState: [Lifecycle.State](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State), block: suspend [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/).() -> T)` Runs the given block on a [CoroutineDispatcher](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/) that executes the block on the main thread and suspends the execution unless the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)'s state is at least minState.  
  
#### Extension properties

##### For [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)

[LifecycleCoroutineScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) |  `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle).[coroutineScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.Lifecycle\).coroutineScope\(\))()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle).  
---|---  
  
##### For [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)

[LifecycleCoroutineScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) |  `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner).[lifecycleScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.LifecycleOwner\).lifecycleScope\(\))()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle).  
---|---  
  
##### For [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)

[CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) |  `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel).[viewModelScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#\(androidx.lifecycle.ViewModel\).viewModelScope\(\))()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel).  
---|---  
  
#### Top-level functions

[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T> |  `[liveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#liveData\(kotlin.coroutines.CoroutineContext,%20kotlin.Long,%20kotlin.coroutines.SuspendFunction1\))(context: [CoroutineContext](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/-coroutine-context/) = EmptyCoroutineContext, timeoutInMs: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) = DEFAULT_TIMEOUT, block: suspend [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope)<T>.() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Builds a LiveData that has values yielded from the given block that executes on a [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope).  
---|---  
[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<T> |  `[liveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#liveData\(java.time.Duration,kotlin.coroutines.CoroutineContext,kotlin.coroutines.SuspendFunction1\))(context: [CoroutineContext](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/-coroutine-context/) = EmptyCoroutineContext, timeout: [Duration](https://developer.android.com/reference/java/time/Duration), block: suspend [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope)<T>.() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Builds a LiveData that has values yielded from the given block that executes on a [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope).  
  
## androidx.navigation

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.navigation:navigation-runtime-ktx:2.10.2"
        implementation "androidx.navigation:navigation-fragment-ktx:2.10.2"
        implementation "androidx.navigation:navigation-ui-ktx:2.10.2"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.navigation:navigation-runtime-ktx:2.10.2")
        implementation("androidx.navigation:navigation-fragment-ktx:2.10.2")
        implementation("androidx.navigation:navigation-ui-ktx:2.10.2")
    }

#### Extension functions

##### For [android.app.Activity](https://developer.android.com/reference/android/app/Activity)

[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) |  `[Activity](https://developer.android.com/reference/android/app/Activity).[findNavController](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(android.app.Activity\).findNavController\(kotlin.Int\))(@IdRes viewId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) given the id of a View and its containing [Activity](https://developer.android.com/reference/android/app/Activity).  
---|---  
[NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy)<Args> |  `[Activity](https://developer.android.com/reference/android/app/Activity).[navArgs](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(android.app.Activity\).navArgs\(\))()` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the Activity's extras as an Args instance.  
  
##### For [android.view.View](https://developer.android.com/reference/android/view/View)

[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) |  `[View](https://developer.android.com/reference/android/view/View).[findNavController](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(android.view.View\).findNavController\(\))()` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) associated with a [View](https://developer.android.com/reference/android/view/View).  
---|---  
  
##### For [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).[activity](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavGraphBuilder\).activity\(kotlin.Int,%20kotlin.Function1\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builder: [ActivityNavigatorDestinationBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigatorDestinationBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a new [ActivityNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Destination)  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).[navigation](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavGraphBuilder\).navigation\(kotlin.Int,%20kotlin.Int,%20kotlin.Function1\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), @IdRes startDestination: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builder: [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a nested [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph)  
  
##### For [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph).[contains](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavGraph\).contains\(kotlin.Int\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns `true` if a destination with `id` is found in this navigation graph.  
---|---  
operator [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination) |  `[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph).[get](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavGraph\).get\(kotlin.Int\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the destination with `id`.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph).[minusAssign](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavGraph\).minusAssign\(androidx.navigation.NavDestination\))(node: [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination))` Removes `node` from this navigation graph.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph).[plusAssign](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavGraph\).plusAssign\(androidx.navigation.NavDestination\))(node: [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination))` Adds a destination to this NavGraph.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph).[plusAssign](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavGraph\).plusAssign\(androidx.navigation.NavGraph\))(other: [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph))` Add all destinations from another collection to this one.  
  
##### For [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)

[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) |  `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).[createGraph](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavController\).createGraph\(kotlin.Int,%20kotlin.Int,%20kotlin.Function1\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 0, @IdRes startDestination: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builder: [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph)  
---|---  
  
##### For [NavHost](https://developer.android.com/reference/kotlin/androidx/navigation/NavHost)

[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) |  `[NavHost](https://developer.android.com/reference/kotlin/androidx/navigation/NavHost).[createGraph](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavHost\).createGraph\(kotlin.Int,%20kotlin.Int,%20kotlin.Function1\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 0, @IdRes startDestination: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builder: [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph)  
---|---  
  
##### For [NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider)

operator T |  `[NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider).[get](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavigatorProvider\).get\(kotlin.String\))(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/))` Retrieves a registered [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator) by name.  
---|---  
operator T |  `[NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider).[get](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavigatorProvider\).get\(kotlin.reflect.KClass\))(clazz: [KClass](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-class/)<T>)` Retrieves a registered [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator) using the name provided by the [Navigator.Name annotation](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.Name).  
[NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) |  `[NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider).[navigation](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavigatorProvider\).navigation\(kotlin.Int,%20kotlin.Int,%20kotlin.Function1\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 0, @IdRes startDestination: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builder: [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph)  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider).[plusAssign](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavigatorProvider\).plusAssign\(androidx.navigation.Navigator\))(navigator: [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator)<out [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination)>)` Register a navigator using the name provided by the [Navigator.Name annotation](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.Name).  
operator [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator)<out [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination)!>? |  `[NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider).[set](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.navigation.NavigatorProvider\).set\(kotlin.String,%20androidx.navigation.Navigator\))(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), navigator: [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator)<out [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination)>)` Register a [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator) by name.  
  
##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navGraphViewModels](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.Int,kotlin.Function0,kotlin.Function0\))(@IdRes navGraphId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), noinline factoryProducer: () -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) = null)` Returns a property delegate to access a [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) scoped to a navigation graph present on the {@link NavController} back stack:  
---|---  
  
#### Top-level functions

[ActivityNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) |  `[ActivityNavigatorExtras](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#ActivityNavigatorExtras\(androidx.core.app.ActivityOptionsCompat,%20kotlin.Int\))(activityOptions: [ActivityOptionsCompat](https://developer.android.com/reference/kotlin/androidx/core/app/ActivityOptionsCompat)? = null, flags: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 0)` Create a new [ActivityNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) instance with a specific [ActivityOptionsCompat](https://developer.android.com/reference/kotlin/androidx/core/app/ActivityOptionsCompat) instance and/or any `Intent.FLAG_ACTIVITY_` flags.  
---|---  
[NavOptions](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions) |  `[navOptions](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#navOptions\(kotlin.Function1\))(optionsBuilder: [NavOptionsBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptionsBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a new [NavOptions](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions)  
  
## androidx.navigation.fragment

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.navigation:navigation-fragment-ktx:2.10.2"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.navigation:navigation-fragment-ktx:2.10.2")
    }

#### Extension functions

##### For [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).[dialog](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.navigation.NavGraphBuilder\).dialog\(kotlin.Int\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Construct a new [DialogFragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination)  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).[dialog](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.navigation.NavGraphBuilder\).dialog\(kotlin.Int,%20kotlin.Function1\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builder: [DialogFragmentNavigatorDestinationBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigatorDestinationBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a new [DialogFragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination)  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).[fragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.navigation.NavGraphBuilder\).fragment\(kotlin.Int\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Construct a new [FragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination)  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder).[fragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.navigation.NavGraphBuilder\).fragment\(kotlin.Int,%20kotlin.Function1\))(@IdRes id: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), builder: [FragmentNavigatorDestinationBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigatorDestinationBuilder).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Construct a new [FragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination)  
  
##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[findNavController](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.fragment.app.Fragment\).findNavController\(\))()` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) given a [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)  
---|---  
[NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy)<Args> |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navArgs](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.fragment.app.Fragment\).navArgs\(\))()` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the Fragment's arguments as an Args instance.  
  
#### Top-level functions

[FragmentNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) |  `[FragmentNavigatorExtras](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#FragmentNavigatorExtras\(kotlin.Array\))(vararg sharedElements: [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<[View](https://developer.android.com/reference/android/view/View), [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)>)` Create a new [FragmentNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) instance with the given shared elements  
---|---  
  
## androidx.navigation.ui

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.navigation:navigation-ui-ktx:2.10.2"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.navigation:navigation-ui-ktx:2.10.2")
    }

#### Extension functions

##### For [android.view.MenuItem](https://developer.android.com/reference/android/view/MenuItem)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[MenuItem](https://developer.android.com/reference/android/view/MenuItem).[onNavDestinationSelected](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(android.view.MenuItem\).onNavDestinationSelected\(androidx.navigation.NavController\))(navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController))` Attempt to navigate to the [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination) associated with this [MenuItem](https://developer.android.com/reference/android/view/MenuItem).  
---|---  
  
##### For [androidx.appcompat.app.AppCompatActivity](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[AppCompatActivity](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity).[setupActionBarWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(androidx.appcompat.app.AppCompatActivity\).setupActionBarWithNavController\(androidx.navigation.NavController,%20androidx.drawerlayout.widget.DrawerLayout\))(navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController), drawerLayout: [DrawerLayout](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout)?)` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar\(\)) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[AppCompatActivity](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity).[setupActionBarWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(androidx.appcompat.app.AppCompatActivity\).setupActionBarWithNavController\(androidx.navigation.NavController,%20androidx.navigation.ui.AppBarConfiguration\))(navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController), configuration: [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) = AppBarConfiguration(navController.graph))` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar\(\)) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
  
##### For [androidx.appcompat.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar).[setupWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(androidx.appcompat.widget.Toolbar\).setupWithNavController\(androidx.navigation.NavController,%20androidx.drawerlayout.widget.DrawerLayout\))(navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController), drawerLayout: [DrawerLayout](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout)?)` Sets up a [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar).[setupWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(androidx.appcompat.widget.Toolbar\).setupWithNavController\(androidx.navigation.NavController,%20androidx.navigation.ui.AppBarConfiguration\))(navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController), configuration: [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) = AppBarConfiguration(navController.graph))` Sets up a [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
  
##### For [com.google.android.material.appbar.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `CollapsingToolbarLayout.[setupWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(com.google.android.material.appbar.CollapsingToolbarLayout\).setupWithNavController\(androidx.appcompat.widget.Toolbar,%20androidx.navigation.NavController,%20androidx.drawerlayout.widget.DrawerLayout\))(toolbar: [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar), navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController), drawerLayout: [DrawerLayout](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout)?)` Sets up a [CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout) and [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `CollapsingToolbarLayout.[setupWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(com.google.android.material.appbar.CollapsingToolbarLayout\).setupWithNavController\(androidx.appcompat.widget.Toolbar,%20androidx.navigation.NavController,%20androidx.navigation.ui.AppBarConfiguration\))(toolbar: [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar), navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController), configuration: [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) = AppBarConfiguration(navController.graph))` Sets up a [CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout) and [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
  
##### For [com.google.android.material.bottomnavigation.BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `BottomNavigationView.[setupWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(com.google.android.material.navigation.NavigationBarView\).setupWithNavController\(androidx.navigation.NavController\))(navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController))` Sets up a [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
---|---  
  
##### For [com.google.android.material.navigation.NavigationView](https://developer.android.com/reference/com/google/android/material/navigation/NavigationView)

[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `NavigationView.[setupWithNavController](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(com.google.android.material.navigation.NavigationView\).setupWithNavController\(androidx.navigation.NavController\))(navController: [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController))` Sets up a [NavigationView](https://developer.android.com/reference/com/google/android/material/navigation/NavigationView) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
---|---  
  
##### For [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).[navigateUp](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(androidx.navigation.NavController\).navigateUp\(androidx.customview.widget.Openable\))(drawerLayout: [DrawerLayout](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout)?)` Handles the Up button by delegating its behavior to the given [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).[navigateUp](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#\(androidx.navigation.NavController\).navigateUp\(androidx.navigation.ui.AppBarConfiguration\))(appBarConfiguration: [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration))` Handles the Up button by delegating its behavior to the given [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController).  
  
#### Top-level functions

[AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) |  `[AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#AppBarConfiguration\(androidx.navigation.NavGraph,androidx.customview.widget.Openable,kotlin.Function0\))(navGraph: [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph), drawerLayout: [DrawerLayout](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout)? = null, noinline fallbackOnNavigateUpListener: () -> [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/ActionBar).  
---|---  
[AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) |  `[AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#AppBarConfiguration\(android.view.Menu,androidx.customview.widget.Openable,kotlin.Function0\))(topLevelMenu: [Menu](https://developer.android.com/reference/android/view/Menu), drawerLayout: [DrawerLayout](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout)? = null, noinline fallbackOnNavigateUpListener: () -> [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/ActionBar).  
[AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) |  `[AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#AppBarConfiguration\(kotlin.collections.Set,androidx.customview.widget.Openable,kotlin.Function0\))(topLevelDestinationIds: [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)>, drawerLayout: [DrawerLayout](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout)? = null, noinline fallbackOnNavigateUpListener: () -> [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/ActionBar).  
  
## androidx.paging

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.paging:paging-common-ktx:2.1.2"
        implementation "androidx.paging:paging-runtime-ktx:2.1.2"
        implementation "androidx.paging:paging-rxjava2-ktx:2.1.2"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.paging:paging-common-ktx:2.1.2")
        implementation("androidx.paging:paging-runtime-ktx:2.1.2")
        implementation("androidx.paging:paging-rxjava2-ktx:2.1.2")
    }

#### Extension functions

##### For [Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)

Flowable<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)<Value>> |  `[DataSource.Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)<Key, Value>.[toFlowable](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#\(androidx.paging.DataSource.Factory\).toFlowable\(androidx.paging.PagedList.Config,kotlin.Any,androidx.paging.PagedList.BoundaryCallback,io.reactivex.Scheduler,io.reactivex.Scheduler,io.reactivex.BackpressureStrategy\))(config: [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config), initialLoadKey: Key? = null, boundaryCallback: [PagedList.BoundaryCallback](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback)<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder).  
---|---  
Flowable<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)<Value>> |  `[DataSource.Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)<Key, Value>.[toFlowable](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#\(androidx.paging.DataSource.Factory\).toFlowable\(kotlin.Int,kotlin.Any,androidx.paging.PagedList.BoundaryCallback,io.reactivex.Scheduler,io.reactivex.Scheduler,io.reactivex.BackpressureStrategy\))(pageSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), initialLoadKey: Key? = null, boundaryCallback: [PagedList.BoundaryCallback](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback)<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder).  
[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)<Value>> |  `[DataSource.Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)<Key, Value>.[toLiveData](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#\(androidx.paging.DataSource.Factory\).toLiveData\(androidx.paging.PagedList.Config,kotlin.Any,androidx.paging.PagedList.BoundaryCallback,java.util.concurrent.Executor\))(config: [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config), initialLoadKey: Key? = null, boundaryCallback: [PagedList.BoundaryCallback](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback)<Value>? = null, fetchExecutor: [Executor](https://developer.android.com/reference/java/util/concurrent/Executor) = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/LivePagedListBuilder).  
[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)<Value>> |  `[DataSource.Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)<Key, Value>.[toLiveData](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#\(androidx.paging.DataSource.Factory\).toLiveData\(kotlin.Int,kotlin.Any,androidx.paging.PagedList.BoundaryCallback,java.util.concurrent.Executor\))(pageSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), initialLoadKey: Key? = null, boundaryCallback: [PagedList.BoundaryCallback](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback)<Value>? = null, fetchExecutor: [Executor](https://developer.android.com/reference/java/util/concurrent/Executor) = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/LivePagedListBuilder).  
Observable<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)<Value>> |  `[DataSource.Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)<Key, Value>.[toObservable](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#\(androidx.paging.DataSource.Factory\).toObservable\(androidx.paging.PagedList.Config,kotlin.Any,androidx.paging.PagedList.BoundaryCallback,io.reactivex.Scheduler,io.reactivex.Scheduler\))(config: [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config), initialLoadKey: Key? = null, boundaryCallback: [PagedList.BoundaryCallback](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback)<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder).  
Observable<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)<Value>> |  `[DataSource.Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)<Key, Value>.[toObservable](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#\(androidx.paging.DataSource.Factory\).toObservable\(kotlin.Int,kotlin.Any,androidx.paging.PagedList.BoundaryCallback,io.reactivex.Scheduler,io.reactivex.Scheduler\))(pageSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), initialLoadKey: Key? = null, boundaryCallback: [PagedList.BoundaryCallback](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback)<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder).  
  
#### Top-level functions

[PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config) |  `[Config](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#Config\(kotlin.Int,%20kotlin.Int,%20kotlin.Boolean,%20kotlin.Int,%20kotlin.Int\))(pageSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), prefetchDistance: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = pageSize, enablePlaceholders: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = true, initialLoadSizeHint: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = pageSize * PagedList.Config.Builder.DEFAULT_INITIAL_PAGE_MULTIPLIER, maxSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = PagedList.Config.MAX_SIZE_UNBOUNDED)` Constructs a [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config), convenience for [PagedList.Config.Builder](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config.Builder).  
---|---  
[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)<Value> |  `[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/package-summary#PagedList\(androidx.paging.DataSource,androidx.paging.PagedList.Config,java.util.concurrent.Executor,java.util.concurrent.Executor,androidx.paging.PagedList.BoundaryCallback,kotlin.Any\))(dataSource: [DataSource](https://developer.android.com/reference/kotlin/androidx/paging/DataSource)<Key, Value>, config: [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config), notifyExecutor: [Executor](https://developer.android.com/reference/java/util/concurrent/Executor), fetchExecutor: [Executor](https://developer.android.com/reference/java/util/concurrent/Executor), boundaryCallback: [PagedList.BoundaryCallback](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback)<Value>? = null, initialKey: Key? = null)` Constructs a [PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList), convenience for [PagedList.Builder](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Builder).  
  
## androidx.palette.graphics

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.palette:palette-ktx:1.0.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.palette:palette-ktx:1.0.0")
    }

#### Extension functions

##### For [Palette](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette)

operator [Palette.Swatch](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette.Swatch)? |  `[Palette](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette).[get](https://developer.android.com/reference/kotlin/androidx/palette/graphics/package-summary#\(androidx.palette.graphics.Palette\).get\(androidx.palette.graphics.Target\))(target: [Target](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Target))` Returns the selected swatch for the given target from the palette, or `null` if one could not be found.  
---|---  
  
## androidx.preference

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.preference:preference-ktx:1.2.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.preference:preference-ktx:1.2.1")
    }

#### Extension functions

##### For [PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup)

operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[contains](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).contains\(androidx.preference.Preference\))(preference: [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference))` Returns `true` if `preference` is found in this preference group.  
---|---  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[forEach](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).forEach\(kotlin.Function1\))(action: (preference: [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action on each preference in this preference group.  
[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[forEachIndexed](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).forEachIndexed\(kotlin.Function2\))(action: (index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), preference: [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Performs the given action on each preference in this preference group, providing its sequential index.  
operator T? |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[get](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).get\(kotlin.CharSequence\))(key: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/))` Returns the preference with `key`, or `null` if no preference with `key` is found.  
operator [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[get](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).get\(kotlin.Int\))(index: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Returns the preference at `index`.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[isEmpty](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).isEmpty\(\))()` Returns true if this preference group contains no preferences.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[isNotEmpty](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).isNotEmpty\(\))()` Returns true if this preference group contains one or more preferences.  
operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)<[Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference)> |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[iterator](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).iterator\(\))()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the preferences in this preference group.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[minusAssign](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).minusAssign\(androidx.preference.Preference\))(preference: [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference))` Removes `preference` from this preference group.  
operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[plusAssign](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).plusAssign\(androidx.preference.Preference\))(preference: [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference))` Adds `preference` to this preference group.  
  
#### Extension properties

##### For [PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup)

[Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)<[Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference)> |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[children](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).children\(\))()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the preferences in this preference group.  
---|---  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup).[size](https://developer.android.com/reference/kotlin/androidx/preference/package-summary#\(androidx.preference.PreferenceGroup\).size\(\))()` Returns the number of preferences in this preference group.  
  
## androidx.room

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.room:room-ktx:2.8.5"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.room:room-ktx:2.8.5")
    }

#### Extension functions

##### For [RoomDatabase](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase)

suspend R |  `[RoomDatabase](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase).[withTransaction](https://developer.android.com/reference/kotlin/androidx/room/package-summary#\(androidx.room.RoomDatabase\).withTransaction\(kotlin.coroutines.SuspendFunction0\))(block: suspend () -> R)` Calls the specified suspending block in a database transaction.  
---|---  
  
## androidx.slice.builders

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.slice:slice-builders-ktx:1.0.0-alpha08"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.slice:slice-builders-ktx:1.0.0-alpha08")
    }

#### Extension functions

##### For [GridRowBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl)

[GridRowBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilder) |  `[GridRowBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl).[cell](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.GridRowBuilderDsl\).cell\(kotlin.Function1\))(buildCell: [CellBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/CellBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
---|---  
[GridRowBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilder) |  `[GridRowBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl).[seeMoreCell](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.GridRowBuilderDsl\).seeMoreCell\(kotlin.Function1\))(buildCell: [CellBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/CellBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
  
##### For [ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl)

[ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) |  `[ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl).[gridRow](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.ListBuilderDsl\).gridRow\(kotlin.Function1\))(buildGrid: [GridRowBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
---|---  
[ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) |  `[ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl).[header](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.ListBuilderDsl\).header\(kotlin.Function1\))(buildHeader: [HeaderBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/HeaderBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
[ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) |  `[ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl).[inputRange](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.ListBuilderDsl\).inputRange\(kotlin.Function1\))(buildInputRange: [InputRangeBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/InputRangeBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
[ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) |  `[ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl).[range](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.ListBuilderDsl\).range\(kotlin.Function1\))(buildRange: [RangeBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/RangeBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
[ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) |  `[ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl).[row](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.ListBuilderDsl\).row\(kotlin.Function1\))(buildRow: [RowBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/RowBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
[ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) |  `[ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl).[seeMoreRow](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#\(androidx.slice.builders.ListBuilderDsl\).seeMoreRow\(kotlin.Function1\))(buildRow: [RowBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/RowBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))`  
  
#### Top-level functions

[Slice](https://developer.android.com/reference/kotlin/androidx/slice/Slice) |  `[list](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#list\(android.content.Context,%20android.net.Uri,%20kotlin.Long,%20kotlin.Function1\))(context: [Context](https://developer.android.com/reference/android/content/Context), uri: [Uri](https://developer.android.com/reference/android/net/Uri), ttl: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), addRows: [ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl).() -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/))` Reduces verbosity required to build a Slice in Kotlin.  
---|---  
[SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction) |  `[tapSliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#tapSliceAction\(android.app.PendingIntent,%20androidx.core.graphics.drawable.IconCompat,%20kotlin.Int,%20kotlin.CharSequence\))(pendingIntent: [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent), icon: [IconCompat](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/IconCompat), imageMode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = ICON_IMAGE, title: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/))` Factory method to build a tappable [SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction).  
[SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction) |  `[toggleSliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#toggleSliceAction\(android.app.PendingIntent,%20androidx.core.graphics.drawable.IconCompat,%20kotlin.CharSequence,%20kotlin.Boolean\))(pendingIntent: [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent), icon: [IconCompat](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/IconCompat)? = null, title: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/), isChecked: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/))` Factory method to build a toggleable [SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction).  
  
## androidx.sqlite.db

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.sqlite:sqlite-ktx:2.7.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.sqlite:sqlite-ktx:2.7.1")
    }

#### Extension functions

##### For [SupportSQLiteDatabase](https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase)

T |  `[SupportSQLiteDatabase](https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase).[transaction](https://developer.android.com/reference/kotlin/androidx/sqlite/db/package-summary#\(androidx.sqlite.db.SupportSQLiteDatabase\).transaction\(kotlin.Boolean,%20kotlin.Function1\))(exclusive: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) = true, body: [SupportSQLiteDatabase](https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase).() -> T)` Run body in a transaction marking it as successful if it completes without exception.  
---|---  
  
## androidx.work

#### Dependency

#### Extension functions

##### For [com.google.common.util.concurrent.ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html)

suspend R |  `[ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html)<R>.[await](https://developer.android.com/reference/kotlin/androidx/work/package-summary#\(androidx.work.Operation\).await\(\))()` Awaits for the completion of the [ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html) without blocking a thread.  
---|---  
  
##### For [Operation](https://developer.android.com/reference/kotlin/androidx/work/Operation)

suspend [Operation.State.SUCCESS](https://developer.android.com/reference/kotlin/androidx/work/Operation.State.SUCCESS)! |  `[Operation](https://developer.android.com/reference/kotlin/androidx/work/Operation).[await](https://developer.android.com/reference/kotlin/androidx/work/package-summary#\(androidx.work.Operation\).await\(\))()` Awaits an [Operation](https://developer.android.com/reference/kotlin/androidx/work/Operation) without blocking a thread.  
---|---  
  
##### For [Data](https://developer.android.com/reference/kotlin/androidx/work/Data)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[Data](https://developer.android.com/reference/kotlin/androidx/work/Data).[hasKeyWithValueOfType](https://developer.android.com/reference/kotlin/androidx/work/package-summary#\(androidx.work.Data\).hasKeyWithValueOfType\(kotlin.String\))(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/))` Returns true if the instance of [Data](https://developer.android.com/reference/kotlin/androidx/work/Data) has a value corresponding to the given key with an expected type T.  
---|---  
  
##### For [Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder)

[OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) |  `[OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder).[setInputMerger](https://developer.android.com/reference/kotlin/androidx/work/package-summary#\(androidx.work.OneTimeWorkRequest.Builder\).setInputMerger\(kotlin.reflect.KClass\))(@NonNull inputMerger: [KClass](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-class/)<out [InputMerger](https://developer.android.com/reference/kotlin/androidx/work/InputMerger)>)` Sets an [InputMerger](https://developer.android.com/reference/kotlin/androidx/work/InputMerger) on the [OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder).  
---|---  
  
#### Top-level functions

[OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) |  `[OneTimeWorkRequestBuilder](https://developer.android.com/reference/kotlin/androidx/work/package-summary#OneTimeWorkRequestBuilder\(\))()` Creates a [OneTimeWorkRequest](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest) with the given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker).  
---|---  
[PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) |  `[PeriodicWorkRequestBuilder](https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder\(kotlin.Long,%20java.util.concurrent.TimeUnit\))(repeatInterval: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), repeatIntervalTimeUnit: [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit))` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker).  
[PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) |  `[PeriodicWorkRequestBuilder](https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder\(java.time.Duration\))(repeatInterval: [Duration](https://developer.android.com/reference/java/time/Duration))` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker).  
[PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) |  `[PeriodicWorkRequestBuilder](https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder\(kotlin.Long,%20java.util.concurrent.TimeUnit,%20kotlin.Long,%20java.util.concurrent.TimeUnit\))(repeatInterval: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), repeatIntervalTimeUnit: [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit), flexTimeInterval: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/), flexTimeIntervalUnit: [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit))` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker).  
[PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) |  `[PeriodicWorkRequestBuilder](https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder\(java.time.Duration,%20java.time.Duration\))(repeatInterval: [Duration](https://developer.android.com/reference/java/time/Duration), flexTimeInterval: [Duration](https://developer.android.com/reference/java/time/Duration))` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker).  
[Data](https://developer.android.com/reference/kotlin/androidx/work/Data) |  `[workDataOf](https://developer.android.com/reference/kotlin/androidx/work/package-summary#workDataOf\(kotlin.Array\))(vararg pairs: [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/)?>)` Converts a list of pairs to a [Data](https://developer.android.com/reference/kotlin/androidx/work/Data) object.  
  
## androidx.work.testing

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "androidx.work:work-testing:2.12.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.work:work-testing:2.12.0")
    }

#### Top-level functions

[TestListenableWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder)<W> |  `[TestListenableWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/package-summary#TestListenableWorkerBuilder\(android.content.Context,%20androidx.work.Data,%20kotlin.collections.List,%20kotlin.Int,%20kotlin.collections.List,%20kotlin.collections.List\))(context: [Context](https://developer.android.com/reference/android/content/Context), inputData: [Data](https://developer.android.com/reference/kotlin/androidx/work/Data) = Data.EMPTY, tags: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> = emptyList(), runAttemptCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 1, triggeredContentUris: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[Uri](https://developer.android.com/reference/android/net/Uri)> = emptyList(), triggeredContentAuthorities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> = emptyList())` Builds an instance of [TestListenableWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder).  
---|---  
[TestWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestWorkerBuilder)<W> |  `[TestWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/package-summary#TestWorkerBuilder\(android.content.Context,%20java.util.concurrent.Executor,%20androidx.work.Data,%20kotlin.collections.List,%20kotlin.Int,%20kotlin.collections.List,%20kotlin.collections.List\))(context: [Context](https://developer.android.com/reference/android/content/Context), executor: [Executor](https://developer.android.com/reference/java/util/concurrent/Executor), inputData: [Data](https://developer.android.com/reference/kotlin/androidx/work/Data) = Data.EMPTY, tags: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> = emptyList(), runAttemptCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) = 1, triggeredContentUris: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[Uri](https://developer.android.com/reference/android/net/Uri)> = emptyList(), triggeredContentAuthorities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> = emptyList())` Builds an instance of [TestWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestWorkerBuilder).  
  
## com.google.android.play.core.ktx

#### Dependency

### Groovy
    
    
    dependencies {
        implementation "com.google.android.play:core-ktx:1.8.1"
    }

### Kotlin
    
    
    dependencies {
        implementation("com.google.android.play:core-ktx:1.8.1")
    }

#### Extension functions

##### For [com.google.android.play.core.appupdate.AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager)

suspend [AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo) |  `[AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager).[requestAppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.appupdate.AppUpdateManager\).requestAppUpdateInfo\(\))()` Requests the update availability for the current app  
---|---  
suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager).[requestCompleteUpdate](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.appupdate.AppUpdateManager\).requestCompleteUpdate\(\))()` For a flexible update flow, triggers the completion of the update.  
Flow<[AppUpdateResult](https://developer.android.com/reference/com/google/android/play/core/ktx/AppUpdateResult)> |  `[AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager).[requestUpdateFlow](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.appupdate.AppUpdateManager\).requestUpdateFlow\(\))()` Entry point for monitoring the availability and progress of updates.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager).[startUpdateFlowForResult](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.appupdate.AppUpdateManager\).startUpdateFlowForResult\(com.google.android.play.core.appupdate.AppUpdateInfo,%20kotlin.Int,%20androidx.fragment.app.Fragment,%20kotlin.Int\))(appUpdateInfo: [AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo), appUpdateType: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/), fragment: Fragment, requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` A version of [AppUpdateManager.startUpdateFlowForResult](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager#startUpdateFlowForResult\(com.google.android.play.core.appupdate.AppUpdateInfo,%20int,%20android.app.Activity,%20int\)) that accepts an AndroidX Fragment for returning the result.  
  
##### For [com.google.android.play.core.splitinstall.SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager)

suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestCancelInstall](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestCancelInstall\(kotlin.Int\))(sessionId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Suspend version of [SplitInstallManager.cancelInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#cancelInstall\(int\))  
---|---  
suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestDeferredInstall](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestDeferredInstall\(kotlin.collections.List\))(moduleNames: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)>)` Suspend version of [SplitInstallManager.deferredInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredInstall\(java.util.List<java.lang.String>\))  
suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestDeferredLanguageInstall](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestDeferredLanguageInstall\(kotlin.collections.List\))(languages: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[Locale](https://developer.android.com/reference/java/util/Locale)>)` Suspend version of [SplitInstallManager.deferredLanguageInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredLanguageInstall\(java.util.List<java.util.Locale>\))  
suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestDeferredLanguageUninstall](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestDeferredLanguageUninstall\(kotlin.collections.List\))(languages: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[Locale](https://developer.android.com/reference/java/util/Locale)>)` Suspend version of [SplitInstallManager.deferredLanguageUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredLanguageUninstall\(java.util.List<java.util.Locale>\))  
suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestDeferredUninstall](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestDeferredUninstall\(kotlin.collections.List\))(moduleNames: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)>)` Suspend version of [SplitInstallManager.deferredUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredUninstall\(java.util.List<java.lang.String>\))  
suspend [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestInstall](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestInstall\(kotlin.collections.List,%20kotlin.collections.List\))(modules: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> = listOf(), languages: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> = listOf())` Initiates installation of the requested modules/languages.  
Flow<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)> |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestProgressFlow](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestProgressFlow\(\))()` Creates and returns a buffered [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) that will deliver all progress events for ongoing split installations.  
suspend [SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestSessionState](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestSessionState\(kotlin.Int\))(sessionId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` Suspend version of [SplitInstallManager.getSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getSessionState\(int\))  
suspend [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)> |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[requestSessionStates](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).requestSessionStates\(\))()` Suspend version of [SplitInstallManager.getSessionStates](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getSessionStates\(\))  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager).[startConfirmationDialogForResult](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallManager\).startConfirmationDialogForResult\(com.google.android.play.core.splitinstall.SplitInstallSessionState,%20androidx.fragment.app.Fragment,%20kotlin.Int\))(sessionState: [SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState), fragment: Fragment, requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/))` A version of [SplitInstallManager.startConfirmationDialogForResult](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#startConfirmationDialogForResult\(com.google.android.play.core.splitinstall.SplitInstallSessionState,%20android.app.Activity,%20int\)) that accepts an AndroidX Fragment for returning the result.  
  
#### Extension properties

##### For [com.google.android.play.core.appupdate.AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo)

[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo).[installStatus](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.appupdate.AppUpdateInfo\).installStatus:kotlin.Int)()` Returns the progress status of the update.  
---|---  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo).[isFlexibleUpdateAllowed](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.appupdate.AppUpdateInfo\).isFlexibleUpdateAllowed:kotlin.Boolean)()` Returns `true` if flexible update is allowed.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo).[isImmediateUpdateAllowed](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.appupdate.AppUpdateInfo\).isImmediateUpdateAllowed:kotlin.Boolean)()` Returns `true` if immediate update is allowed.  
  
##### For [com.google.android.play.core.install.InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState)

[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState).[hasTerminalStatus](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.install.InstallState\).hasTerminalStatus:kotlin.Boolean)()` This signifies that this is a terminal status (there will be no more updates) and should be handled accordingly (success, cancellation or failure).  
---|---  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState).[installErrorCode](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.install.InstallState\).installErrorCode:kotlin.Int)()` Returns the error code for an install, or {@link InstallErrorCode#NO_ERROR}.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState).[installStatus](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.install.InstallState\).installStatus:kotlin.Int)()` Returns the status of an install.  
[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)! |  `[InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState).[packageName](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.install.InstallState\).packageName:kotlin.String)()` Returns the package name for the app being installed.  
  
##### For [com.google.android.play.core.splitinstall.SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)

[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[bytesDownloaded](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).bytesDownloaded:kotlin.Long)()` The bytes downloaded by this update.  
---|---  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[errorCode](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).errorCode:kotlin.Int)()` The error code of this update.  
[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[hasTerminalStatus](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).hasTerminalStatus:kotlin.Boolean)()` Signifies that this update is terminal, meaning there will be no more updates for this session.  
[List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[languages](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).languages:kotlin.collections.List)()` The languages included by this update.  
[List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[moduleNames](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).moduleNames:kotlin.collections.List)()` The modules included by this update.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[sessionId](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).sessionId:kotlin.Int)()` The session id of this update.  
[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[status](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).status:kotlin.Int)()` The status code of this update.  
[Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) |  `[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState).[totalBytesToDownload](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#\(com.google.android.play.core.splitinstall.SplitInstallSessionState\).totalBytesToDownload:kotlin.Long)()` The total bytes to download by this update.  
  
#### Top-level functions

[SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener) |  `[SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#SplitInstallStateUpdatedListener\(kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1\))(onRequiresConfirmation: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/), onInstalled: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/), onFailed: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onPending: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onDownloaded: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onDownloading: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onInstalling: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onCanceling: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onCanceled: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onNonTerminalStatus: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {}, onTerminalStatus: ([SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) = {})` A convenience function for creating a [SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener).  
---|---  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
