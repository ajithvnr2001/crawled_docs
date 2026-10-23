---
url: https://developer.android.com/training/testing/fundamentals/test-doubles/
title: Use test doubles in Android \u00a0|\u00a0 Test your app on Android \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:53.678557+00:00
---

# Use test doubles in Android  |  Test your app on Android  |  Android Developers

> Source: https://developer.android.com/training/testing/fundamentals/test-doubles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Test your app on Android ](https://developer.android.com/training/testing)



#  Use test doubles in Android Stay organized with collections  Save and categorize content based on your preferences. 

When you test an element or system of elements you do it in _isolation_. For example, to test a ViewModel you don't need to start an emulator and launch a UI because it doesn't (or shouldn't) depend on the Android framework.

However, the subject under test might _depend_ on others for it to work. For instance, a ViewModel might depend on a data repository to work.

When you need to provide a dependency to a subject under test, a common practice is to create a _test double_ (or _test object_). Test doubles are objects that look and act as components in your app but they're created in your test to provide a specific behavior or data. The main advantages are that they make your tests faster and simpler.

## Types of test doubles

There are various types of test doubles:

Fake  | A test double that has a "working" implementation of the class, but it is implemented in a way that makes it good for tests but unsuitable for production.  Example: an in-memory database.  Fakes don't require a mocking framework and are lightweight. They are **preferred**.   
---|---  
Mock  | A test double that behaves how you program it to behave and that has expectations about its interactions. Mocks will fail tests if their interactions don't match the requirements that you define. Mocks are usually created with a _mocking framework_ to achieve all this.  Example: Verify that a method in a database was called exactly once.   
Stub  | A test double that behaves how you program it to behave but doesn't have expectations about its interactions. Usually created with a mocking framework. Fakes are preferred over stubs for simplicity.   
Dummy  | A test double that is passed around but not used, such as if you just need to provide it as a parameter.  Example: an empty function passed as a click callback.   
Spy  | A wrapper over a real object which also keeps track of some additional information, similar to mocks. They are usually avoided for adding complexity. Fakes or mocks are therefore preferred over spies.   
Shadow  | Fake used in Robolectric.   
**Caution:** There are conflicting definitions depending on the source. A comprehensive source is [_Mocks aren't Stubs_](https://martinfowler.com/articles/mocksArentStubs.html) by Martin Fowler.**Note:** When using a library or framework, check with the authors to see if they provide any officially-supported testing infrastructures, such as fakes, that you can reliably depend on.

## Example using a fake

Suppose that you want to unit test a ViewModel that depends on an interface called `UserRepository` and exposes the name of the first user to a UI. You can create a fake test double by implementing the interface and returning known data.
    
    
    object FakeUserRepository : UserRepository {
        fun getUsers() = listOf(UserAlice, UserBob)
    }
    
    val const UserAlice = User("Alice")
    val const UserBob = User("Bob")
    

This fake `UserRepository` does not need to depend on the local and remote data sources that the production version would use. The file lives in the test source set and will not ship with the production app.

![A fake dependency can return known data without depending on remote data sources](https://developer.android.com/static/training/testing/fundamentals/fake-deps.png)**Figure 1** : A fake dependency in a unit test.

The following test verifies that the ViewModel correctly exposes the first user name to the view.
    
    
    @Test
    fun viewModelA_loadsUsers_showsFirstUser() {
        // Given a VM using fake data
        val viewModel = ViewModelA(FakeUserRepository) // Kicks off data load on init
    
        // Verify that the exposed data is correct
        assertEquals(viewModel.firstUserName, UserAlice.name)
    }
    

Replacing the `UserRepository` with a fake is easy in a unit test, because the ViewModel is created by the tester. However, it can be challenging to replace arbitrary elements in bigger tests.

## Replacing components and dependency injection

When tests have no control over the creation of the systems under test, replacing components for test doubles becomes more involved and requires the architecture of your app to follow a _testable_ design.

Even big end-to-end tests can benefit from using test doubles, such as an instrumented UI test that navigates through a full user flow in your app. In that case you might want to make your test _hermetic_. A hermetic test avoids all external dependencies, such as fetching data from the internet. This improves reliability and performance.

![](https://developer.android.com/static/training/testing/fundamentals/bigtest.png)**Figure 2** : A big test that covers most of the app and fakes remote data.

You can design your app to achieve this flexibility manually, but we recommend using a [dependency injection](https://developer.android.com/training/dependency-injection) framework like [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) to replace components in your app at test time. See the [Hilt testing guide.](https://developer.android.com/training/dependency-injection/hilt-testing)

**Note:** On Android, you can also use the [Robolectric](https://developer.android.com/training/testing/local-tests/robolectric) framework, which provides a special type of test double, called shadows.

## Next steps

The [Testing strategies](https://developer.android.com/training/testing/fundamentals/strategies) page shows how you can improve your productivity using different types of tests.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
