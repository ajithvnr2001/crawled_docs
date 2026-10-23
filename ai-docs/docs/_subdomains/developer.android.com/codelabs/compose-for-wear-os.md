---
url: https://developer.android.com/codelabs/compose-for-wear-os/
title: Compose for Wear OS Codelab \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:35:06.706664+00:00
---

# Compose for Wear OS Codelab  |  Android Developers

> Source: https://developer.android.com/codelabs/compose-for-wear-os/




#  Compose for Wear OS Codelab Stay organized with collections  Save and categorize content based on your preferences. 

##  1\. Introduction 

![2c9dd335c9d65f10.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/2c9dd335c9d65f10.png)

Compose for Wear OS lets you translate the knowledge you've learned building apps with Jetpack Compose to wearable devices.

With built-in support for Material Design, Compose for Wear OS [simplifies and accelerates UI development](https://developer.android.com/jetpack/compose/why-adopt#less-code) and helps you create beautiful apps with less code.

For this codelab, we expect you to have some knowledge of Compose, but you certainly don't need to be an expert.

You will create several Wear specific composables (both simple and complex), and, by the end, you can start writing your own apps for Wear OS. Let's get started!

## What you will learn

  * Similarities/differences between your previous experience with Compose
  * Simple composables and how they work on Wear OS
  * Wear OS specific composables
  * Wear OS's `LazyColumn` (`TransformingLazyColumn`)
  * Wear OS's version of the `Scaffold`



## What you will build

You'll build a simple app that displays a scrollable list of composables optimized for Wear OS.

Because you will be using [AppScaffold](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold\(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1\)) and [ScreenScaffold](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScreenScaffold\(androidx.compose.ui.Modifier,androidx.wear.compose.foundation.ScrollInfoProvider,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,kotlin.Function2\)),you'll also get a curved text time at the top and a scrolling indicator tied to the side of the device.

Here's what it will look like when you are finished with the code lab:

![3162140d003d8e31.gif](https://developer.android.com/static/codelabs/compose-for-wear-os/img/3162140d003d8e31.gif)

## Prerequisites

  * Basic understanding of [Android development](https://developer.android.com/)
  * Basic understanding of [Kotlin](https://developer.android.com/kotlin)
  * Basic knowledge of [Compose](https://developer.android.com/jetpack/compose)



##  2\. Getting Set Up 

In this step, you will set up your environment and download the starter project.

## What you will need

  * Latest stable version of [Android Studio](https://developer.android.com/studio)
  * Wear OS device or emulator (New to this? [Here's](https://developer.android.com/training/wearables/apps/creating#emulator) how to set it up.)



## Download code

If you have git installed, you can simply run the command below to clone the code from [this repo](https://github.com/android/codelab-compose-for-wear-os). To check whether git is installed, type `git --version` in the terminal or command line and verify that it executes correctly.
    
    
    git clone https://github.com/android/codelab-compose-for-wear-os.git
    cd codelab-compose-for-wear-os
    

If you do not have git, you can click the following button to download all the code for this codelab:

[file_downloadDownload ZIP](https://github.com/android/codelab-compose-for-wear-os/archive/main.zip)

The sample directory contains the **start** and **finished** code for this codelab. In the Project view on the left of Android Studio you will find two modules.

  * ![d61ffd479bdbcb9f.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/d61ffd479bdbcb9f.png)**start** – the starter code for this project; you will make changes to this to complete the codelab
  * ![d61ffd479bdbcb9f.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/d61ffd479bdbcb9f.png)**finished** – the completed code for this codelab; used to check your work



At any time you can run either module in Android Studio by changing the run configuration in the toolbar.

![51cb2645eece1f20.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/51cb2645eece1f20.png)

## Open project in Android Studio

  1. On the Welcome to Android Studio window select ![c01826594f360d94.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/c01826594f360d94.png)**Open...**
  2. Select the folder **`[Download Location]`**
  3. When Android Studio has imported the project, test that you can run the `start` and `finished` modules on a Wear OS emulator or physical device.
  4. The `start` module should look like the screenshot below. It's where you will be doing all your work.



![271451f93a57db41.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/271451f93a57db41.png)

## Explore the start code

  * `build.gradle` contains a basic app configuration. It includes the dependencies necessary to create a Composable Wear OS App. We'll discuss what's similar and different between Jetpack Compose and the Wear OS version.
  * `main > AndroidManifest.xml` includes the elements necessary to create a Wear OS application. This is the same as a non-Compose app and similar to a mobile app, so we won't review this.
  * `main > theme/` folder contains the `Color`, `Type`, and `Theme` files used by Compose for the theme.
  * `main > MainActivity.kt` contains boilerplate for creating an app with Compose. It also contains the top-level composables (like the `Scaffold` and `TransformingLazyColumn`) for our app.
  * `main > ReusableComponents.kt` contains functions for most of the Wear specific composables we'll create. We will do a lot of our work in this file.



##  3\. Review the dependencies 

Most of the Wear related dependency changes you make will be at the top [architectural layers](https://developer.android.com/jetpack/compose/layering) (highlighted in red below).

![d92519e0b932f964.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/d92519e0b932f964.png)

That means many of the dependencies you already use with Jetpack Compose don't change when targeting Wear OS. For example, the UI, Runtime, Compiler, and Animation dependencies will remain the same.

However, you will need to use the proper Wear OS **Material** , **Foundation** , and **Navigation** libraries which are different from the libraries you have used before.

Below is a comparison to help clarify the differences:

**Wear OS Dependency**(androidx.wear.*) | **Comparison** | **Standard Dependency**(androidx.*)  
---|---|---  
[androidx.wear.compose:compose-material3](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary) | **_instead of_** | androidx.compose.material:material **₁**  
[androidx.wear.compose:compose-navigation](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary) | **_instead of_** | androidx.navigation:navigation-compose  
[androidx.wear.compose:compose-foundation](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/package-summary) | **_in addition to_** | androidx.compose.foundation:foundation  
[androidx.wear.compose:compose-ui-tooling](https://developer.android.com/reference/kotlin/androidx/wear/compose/ui/tooling/preview/package-summary) | **_in addition to_** | androidx.compose.ui:ui-tooling-preview  
  
_1\. Developers can continue to use other material related libraries like material ripple and material icons extended with the Wear Compose Material library. Alternatively to compose-material3 version, you can use_[ _androidx.wear.compose:compose-material_](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary) _but you shouldn't be mixing Material 3 and Material 2.5 in the same app. We advise you to use material3 as it supports Material 3 Expressive design._

**Note:** While it's technically possible to use the standard dependencies on Wear OS, we always recommend using the wear-specific versions for the best experience.

Open the `build.gradle`, search for "**`TODO: Review Dependencies`** " in your `start` module. (This step is just to review the dependencies, you will not be adding any code.)

start/build.gradle:
    
    
    dependencies {
        val composeBom = platform(libs.androidx.compose.bom)
    
        // General compose dependencies
        implementation(composeBom)
        implementation(libs.androidx.activity.compose)
        implementation(libs.compose.ui.tooling.preview)
    
        implementation(libs.androidx.material.icons.extended)
    
        // Compose for Wear OS Dependencies
        implementation(libs.wear.compose.material)
    
        // Foundation is additive, so you can use the mobile version in your Wear OS app.
        implementation(libs.wear.compose.foundation)
    
        // Compose preview annotations for Wear OS.
        implementation(libs.androidx.compose.ui.tooling)
    
        implementation(libs.horologist.compose.layout)
    
        coreLibraryDesugaring(libs.desugar.jdk.libs)
    
        debugImplementation(libs.compose.ui.tooling)
        debugImplementation(libs.androidx.ui.test.manifest)
        debugImplementation(composeBom)
    }
    

You should recognize many of the general Compose dependencies, so we won't cover those.

Let's move to the Wear OS dependencies.

Just as outlined earlier, only the Wear OS specific version of **`material`** (`androidx.wear.compose:compose-material3`) is included. That is, you will not see or include `androidx.compose.material:material3` in your project.

It's important to call out that you can use other material libraries with Wear Material. We actually do that in this codelab by including `androidx.compose.material:material-icons-extended`.

Finally, we include the Wear **`foundation`** library for Compose (`androidx.wear.compose:compose-foundation`) . This is additive, so you can use it with the standard **`foundation`** you've used before. In fact, you probably already recognized we included it in the general compose dependencies!

Ok, now that we understand the dependencies, let's have a look at the main app.

##  4\. Review MainActivity 

**We will do all our work in the**

**`start`**

**module, so make sure every file you open is in there.**

Let's start by opening `MainActivity` in the `start` module.

This is a pretty simple class that extends `ComponentActivity` and uses `setContent { WearApp() }` to create the UI.

From your previous knowledge of Compose, this should look familiar to you. We are just setting up the UI.

Scroll down to the `WearApp()` composable function. Before we talk about the code itself, you should see a bunch of TODOs scattered throughout the code. These each represent steps in this codelab. You can ignore them for now.

It should look something like this:

**Code in fun WearApp():**
    
    
    WearAppTheme {
         /* *************************** Part 4: Wear OS Scaffold *************************** */
        // TODO (Start): Create a AppScaffold (Wear Version)
    
        // TODO: Swap to TransformingLazyColumnState
        val listState = rememberLazyListState()
    
        /* *************************** Part 4: Wear OS Scaffold *************************** */
        // TODO (Start): Create a ScreenScaffold (Wear Version)
    
        /* *************************** Part 3: ScalingLazyColumn *************************** */
        // TODO: Swap a TransformingLazyColumn (Wear's version of LazyColumn)
        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            state = listState,
        ) {
            // TODO: Remove item; for beginning only.
            item { StartOnlyTextComposables() }
    
            /* ******************* Part 1: Simple composables ******************* */
            item { ButtonExample() }
            item { TextExample() }
            item { CardExample() }
    
            /* ********************* Part 2: Wear unique composables ********************* */
            item { ChipExample() }
            item { ToggleChipExample() }
            }
    
        // TODO (End): Create a ScreenScaffold (Wear Version)
        // TODO (End): Create a AppScaffold (Wear Version)
    }
    

We start by setting the theme, `WearAppTheme { }`. This is exactly the same way you've written it before, that is, you set a [`MaterialTheme`](https://developer.android.com/develop/ui/compose/designsystems/material3) with colors, typography, and shapes.

However, in the case of Wear OS, we generally recommend using the default [Material Wear shapes](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/Shapes) which are optimized for round devices, so if you dive into our `theme/Theme.kt`, you can see we don't override shapes.

If you wish, you can open the `theme/Theme.kt` to explore it further, but, again, it's the same as on the phone.

We then create a [`LazyColumn`](https://developer.android.com/jetpack/compose/lists) which is used to produce a vertically scrolling list for a bunch of items (just like you did before).

**Code:**
    
    
    item { StartOnlyTextComposables() }
    
    /* ******************* Part 1: Simple composables ******************* */
    item { ButtonExample() }
    item { TextExample() }
    item { CardExample() }
    
    /* ********************* Part 2: Wear unique composables ********************* */
    item { ChipExample() }
    item { ToggleChipExample() }
    

For the items themselves, only `StartOnlyTextComposables()` produces any UI. (We will populate the rest throughout the code lab.)

These functions are actually in the `ReusableComponents.kt` file, which we will visit in the next section.

Let's get started with Compose for Wear OS!

##  5\. Add Simple Composables 

We'll start with three composables (`Button`, `Text`, and `Card`) that you are probably already familiar with.

First, we are going to remove the hello world composable.

Search for "**`TODO: Remove item`** " and **erase** both the comment and the line below it:

**Step 1**
    
    
    // TODO: Remove item; for beginning only.
    item { StartOnlyTextComposables() }
    

Next, let's add our first composable.

## Create a Icon Button composable

Open `ReusableComponents.kt` in the `start` module and search for "**`TODO: Create a Icon Button Composable`** " and replace the current composable method with this code.

**Step 2**
    
    
    // TODO: Create a Icon Button Composable
    @Composable
    fun IconButtonExample(
        modifier: Modifier = Modifier,
    ) {
        FilledIconButton(
            onClick = { /* ... */ },
            modifier = modifier,
        ) {
            Icon(
                imageVector = Icons.Rounded.Phone,
                contentDescription = "triggers phone action",
            )
        }
    }
    

The `IconButtonExample()` composable function (where this code exists) will now generate a centered button.

Let's walk through the code.

We use a [`FilledIconButton`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/FilledIconButton.composable#FilledIconButton\(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.String,kotlin.Boolean,androidx.wear.compose.material3.IconButtonShapes,androidx.wear.compose.material3.IconButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1\)) which is a circular, icon-only button with a colored background and a contrasting content color. It offers a single slot to take an icon or image.

After that, we set the click event to an empty lambda. In our case, these composables are just for a demo, so we won't need that. However, in a real app, we'd communicate with a, for example, ViewModel to perform business logic.

Then we set an Icon inside our button. This code is the same as you have seen for an `Icon` before. We are also getting our icon from the `androidx.compose.material:material-icons-extended` library.

Finally, you don't need to worry about centering the button at this stage since it will be fixed later automatically when migrating from `LazyColumn` to `TransformingLazyColumn.`

If you run the app, you should get something like this, **don't worry if the button is not centered for now** :

![9346dbd2b8bc6a56.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/9346dbd2b8bc6a56.png)

This is code you have probably already written before (which is great). The difference is now you get a button optimized for Wear OS.

Pretty straightforward, let's look at another one.

## Create a Text composable

In `ReusableComponents.kt`, search for "**`TODO: Create a Text Composable`** " and replace the current composable method with this code.

**Step 3**
    
    
    // TODO: Create a Text Composable
    @Composable
    fun TextExample(modifier: Modifier = Modifier) {
       ListHeader{
          Text(
               modifier = modifier
                   .fillMaxWidth(),
               textAlign = TextAlign.Center,
               text = stringResource(R.string.hello_compose_codelab),
           )
       }
    }
    

We create the [`Text`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#Text\(kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Function1,androidx.compose.ui.text.TextStyle\)) composable, set its modifier, align the text, set a color, and finally set the text itself from a String resource. Since we are going to add a List later, we are wrapping this text into a [`ListHeader`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/ListHeader.composable#ListHeader\(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.PaddingValues,androidx.wear.compose.material3.SurfaceTransformation,kotlin.Function1\)) so that the content will be start and end padded.

Text composables should look very familiar to Compose developers and the code is actually identical to the code you've used before.

Let's see what it looks like:

![dcad71112a91d706.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/dcad71112a91d706.png)

The `TextExample()` composable function (where we placed our code) now produces a Text composable in our main material color. The string is pulled from our `res/values/strings.xml` file.

So far, so good. Let's look at our last similar composable, `Card`.

## Create a Card composable

In `ReusableComponents.kt`, search for "**`TODO: Create a Card`** " and replace the current composable method with this code.

**Step 4**
    
    
    // TODO: Create a Card (specifically, an AppCard) Composable
    @Composable
    fun CardExample(
        modifier: Modifier = Modifier,
        iconModifier: Modifier = Modifier
    ) {
        AppCard(
            modifier = modifier,
            appImage = {
                Icon(
                    imageVector = Icons.AutoMirrored.Rounded.Message,
                    contentDescription = "triggers open message action",
                    modifier = iconModifier
                )
            },
            appName = { Text("Messages") },
            time = { Text("12m") },
            title = { Text("Kim Green") },
            onClick = { /* ... */ }
        ) {
            Text("On my way!")
        }
    }
    

Wear is a little different in that we have two major cards, [`AppCard`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AppCard\(kotlin.Function0,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.graphics.painter.Painter,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1\)) and [`TitleCard`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#TitleCard\(kotlin.Function0,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.graphics.painter.Painter,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1\)).

In our case, we want an [`Icon`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/Icon.composable#Icon\(androidx.compose.ui.graphics.vector.ImageVector,kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color\)) in our card, so we are going to use `AppCard`. (`TitleCard` has less slots, see [Cards](https://developer.android.com/training/wearables/compose/cards) guide for more information.)

We create the `AppCard` composable, set its modifier, add an `Icon`, add several `Text` composable parameters (each for a different space on the card), and finally set the main content text at the end.

Let's see what it looks like, don't worry about adding additional bottom padding as this will be fixed when migrating from `LazyColumn` to `TransformingLazyColumn` :

![faf2fe359baf0946.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/faf2fe359baf0946.png)

At this point, you probably recognize that for these composables the Compose code is virtually the same as you've used before which is great, right? You get to reuse all that knowledge you've already gained!

Ok, let's look at some new composables.

##  6\. Add Wear Unique Composables 

For this section, we will explore the `Chip` and `ToggleChip` composables.

## Create a Chip composable

[Chips](https://material.io/components/chips) are meant to be a quick, one tap action, which makes especially good sense for a Wear device with limited screen real estate.

You can implement a Chip by using a [`Button`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#Button\(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.wear.compose.material3.ButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1\)). Here's a couple variations of the [`Button`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#Button\(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.wear.compose.material3.ButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1\)) composable function to give you an idea of what you can create:

![13c7dc5e08b5d2d4.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/13c7dc5e08b5d2d4.png)![9859b3f9880f75af.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/9859b3f9880f75af.png)

Let's write some code.

In `ReusableComponents.kt`, search for "**`TODO: Create a Chip`** " and replace the current composable method with this code.

**Step 5**
    
    
    // TODO: Create a Chip Composable
    @Composable
    fun ChipExample(
        modifier: Modifier = Modifier,
    ) {
        Button(
            modifier = modifier,
            onClick = { /* ... */ },
            icon = {
                Icon(
                    imageVector = Icons.Rounded.SelfImprovement,
                    contentDescription = "triggers meditation action",
                )
            },
        ) {
            Text(
                text = "5 minute Meditation",
                maxLines = 1,
                overflow = TextOverflow.Ellipsis,
            )
        }
    }
    

The `Button` composable uses many of the same parameters as you are used to with other composables (modifier and `onClick`), so we don't need to review those.

It also takes an icon and a content Slot for composable body content displayed on the Button (which we create a `Text` composable for).

The `Icon` code should look exactly the same as the code you saw in other composables, but for this one, we are pulling the `Self Improvement` icon from the `androidx.compose.material:material-icons-extended` library.

Let's see what it looks like (remember to scroll down), don't worry about adding additional bottom padding as this will be fixed when migrating from `LazyColumn` to `TransformingLazyColumn` :

![22afab093efc7fc5.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/22afab093efc7fc5.png)

Ok, let's look at a variation on `Button`, the `SwitchButton` composable.

## Create a SwitchChip composable

`SwitchButton` is just like a `Button` but allows the user to interact with a switch.

![eb38c8acb3ac996.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/eb38c8acb3ac996.png)

In `ReusableComponents.kt`, search for "**`TODO: Create a SwitchChip`** " and replace the current composable method with this code.

**Step 6**
    
    
    // TODO: Create a Switch Chip Composable
    @Composable
    fun SwitchChipExample(modifier: Modifier = Modifier) {
        var checked by remember { mutableStateOf(true) }
        SwitchButton(
            modifier = modifier.fillMaxWidth(),
            label = {
                Text(
                    "Sound",
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis,
                    modifier = Modifier.semantics {
                        this.contentDescription = if (checked) "On" else "Off"
                    },
                )
            },
            checked = checked,
            onCheckedChange = { checked = it },
            enabled = true,
        )
    }
    

Now the `SwitchChipExample()` composable function (where this code exists) generates a `SwitchChip` using a switch toggle (instead of a checkbox or radio button).

First, we create a `MutableState`. We haven't been doing this in the other functions, because we are mainly doing UI demos so you can see what Wear offers.

In a normal app, you would probably want to pass in the checked state and the lambda for handling the tap, so the composable can be stateless ( [more info here](https://developer.android.com/jetpack/compose/state#stateful-vs-stateless)).

In our case, we are just keeping it simple to show off what the `SwitchChip` looks like in action with a working toggle (even though we don't do anything with the state).

Next, we set the checked state, and the toggle control to give us the switch we want.

We then create a lambda for changing the state and finally set the label with a `Text` composable (and some basic parameters).

Let's see what it looks like:

![8ef93a35bdb7302a.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/8ef93a35bdb7302a.png)

Ok, now you've seen a lot of Wear OS specific composables and, as stated before, most of the code is almost the same as what you've written before.

Let's look at something a little more advanced.

##  7\. Migrate to TransformingScalingLazyColumn 

You probably have used [`LazyColumn`](https://developer.android.com/jetpack/compose/lists#lazy) in your mobile apps to produce a vertically scrolling list.

Because a round device is smaller at the top and bottom, there is less space to show items. Therefore, Wear OS has its own version of `LazyColumn` to better support those round devices.

[Transforming`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/package-summary#TransformingLazyColumn\(androidx.compose.foundation.layout.PaddingValues,androidx.compose.ui.Modifier,androidx.wear.compose.foundation.lazy.TransformingLazyColumnState,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,kotlin.Function1\)) extends `LazyColumn` to support both scaling and transparency at the top and bottom of the screen to make the content more readable to the user.

Here's a demo:

![c056381ba4a7475d.gif](https://developer.android.com/static/codelabs/compose-for-wear-os/img/c056381ba4a7475d.gif)

Notice how as the item gets near the center it scales up to its full size and then as it moves away it scales back down (along with getting more transparent).

Here is a more concrete example from an app:

![6dbb1e13f99e5e1f.gif](https://developer.android.com/static/codelabs/compose-for-wear-os/img/6dbb1e13f99e5e1f.gif)

We've found this really helps with readability.

Now that you've seen [`TransformingLazyColumn`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/package-summary#TransformingLazyColumn\(androidx.compose.foundation.layout.PaddingValues,androidx.compose.ui.Modifier,androidx.wear.compose.foundation.lazy.TransformingLazyColumnState,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,kotlin.Function1\)) in action, let's get started converting our `LazyColumn`.

## Convert to a TransformingLazyColumnState

In `MainActivity.kt`, search for "**`TODO: Swap to TransformingLazyColumnState`** " and replace that comment and line below with this code, note how we specify which ones are the first and last component so that the best padding values are used to avoid any content clipping.

**Step 7**
    
    
    // TODO: Swap to TransformingLazyColumnState
    val listState = rememberTransformingLazyColumnState()
    val transformationSpec = rememberTransformationSpec()
    

The names are almost identical. Just like `LazyListState` handles state for a `LazyColumn`, `TransformingLazyColumnState` handles it for a `TransformingLazyColumn`.

We also specify a [`transformationSpec`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/lazy/TransformationSpec) here so that we can add transformations for the items as they scroll across the screen.

## Convert to a TransformingLazyColumn

Next we swap in `TransformingLazyColumn`.

In `MainActivity.kt`, search for "**`TODO: Swap a TransformingLazyColumn`** ". First, replace `LazyColumn` with `TransformingLazyColumn`.

Then remove `contentPadding, verticalArrangement` and `modifier` altogether - `TransformingLazyColumn` already provides default settings that guarantee a better default visual effect as most of the viewport will be filled with list items. In most cases default parameters will be sufficient, if you have header on top we recommend putting it into [`ListHeader`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ListHeader\(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1\)) as a first item.

**Step 8**
    
    
    // TODO: Swap a TransformingLazyColumn (Wear's version of LazyColumn)
    TransformingLazyColumn(
        state = listState,
        contentPadding = contentPadding)
    

## Add a scroll transform effect to items

Now we add a ShapeMorphing effect to our `TransformingLazyColumn` elements by using the following `Modifier` and `SurfaceTransformation`. Apply the same code to all the components (

except `IconButtonExample` which doesn't support this feature yet)`.`

**Step 9**
    
    
    TextExample(
       modifier = Modifier.fillMaxWidth().transformedHeight(this, transformationSpec),
       transformation = SurfaceTransformation(transformationSpec),
    )
    

That's it! Let's see what it looks like:

![4c97e27b6acb83ef.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/4c97e27b6acb83ef.png)

You can see the content is scaled and the transparency is adjusted at the top and bottom of the screen as you scroll with very little work to migrate!

You can really notice it with the meditation composables as you move it up and down.

Now onto the last topic, Wear OS's `Scaffold`.

##  8\. Add a Scaffold 

[AppScaffold](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold\(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1\)) and [ScreenScaffold](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScreenScaffold\(androidx.wear.compose.foundation.lazy.ScalingLazyListState,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,kotlin.Function2\)) provide a layout structure to help you arrange screens in common patterns, just like mobile, but instead of an [App Bar, FAB, Drawer, or other mobile specific elements](https://developer.android.com/jetpack/compose/layouts/material#scaffold), it supports three Wear specific layouts with top-level components: time, scroll/position indicator and the page indicator.

Here's what they look like:

![](https://developer.android.com/static/codelabs/compose-for-wear-os/img/ca4baa1c6f01e9a7.png) | [`TimeText`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#TimeText\(androidx.compose.ui.Modifier,androidx.wear.compose.material.TimeSource,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1\))  
---|---  
![](https://developer.android.com/static/codelabs/compose-for-wear-os/img/b60ff4d19fc7615b.png) | [`ScrollIndicator`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScrollIndicator\(androidx.compose.foundation.lazy.LazyListState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.animation.core.AnimationSpec\))  
![](https://developer.android.com/static/codelabs/compose-for-wear-os/img/c8e67bda83f311ac.png) | [`HorizontalPageIndicator`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/HorizontalPageIndicator.composable#HorizontalPageIndicator\(androidx.wear.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color\))  
  
We'll look at the first three components in detail, but, first, let's put the scaffold in place.

The scaffold components [`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold\(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1\)) and [`ScreenScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScreenScaffold\(androidx.wear.compose.foundation.lazy.ScalingLazyListState,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,kotlin.Function2\)) lay out the structure of a screen and coordinate transitions of the [`ScrollIndicator`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScrollIndicator\(androidx.compose.foundation.ScrollState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.animation.core.AnimationSpec\)) and [`TimeText`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#TimeText\(androidx.compose.ui.Modifier,androidx.wear.compose.foundation.CurvedModifier,kotlin.Float,androidx.wear.compose.material3.TimeSource,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2\)) components.

[`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold\(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1\)) allows static screen elements such as [`TimeText`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#TimeText\(androidx.compose.ui.Modifier,androidx.wear.compose.foundation.CurvedModifier,kotlin.Float,androidx.wear.compose.material3.TimeSource,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2\)) to remain visible during in-app transitions such as swipe-to-dismiss. [`ScreenScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScreenScaffold\(androidx.wear.compose.foundation.lazy.ScalingLazyListState,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,kotlin.Function2\)) displays the [`ScrollIndicator`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/ScrollIndicator.composable#ScrollIndicator\(androidx.compose.foundation.ScrollState,androidx.compose.ui.Modifier,androidx.wear.compose.material3.ScrollIndicatorColors,kotlin.Boolean,androidx.compose.animation.core.AnimationSpec\)) at the center-end of the screen by default and coordinates showing/hiding [`TimeText`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/TimeText.composable#TimeText\(androidx.compose.ui.Modifier,androidx.wear.compose.foundation.CurvedModifier,kotlin.Float,androidx.compose.ui.graphics.Color,androidx.wear.compose.material3.TimeSource,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2\)) and [`ScrollIndicator`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/ScrollIndicator.composable#ScrollIndicator\(androidx.compose.foundation.ScrollState,androidx.compose.ui.Modifier,androidx.wear.compose.material3.ScrollIndicatorColors,kotlin.Boolean,androidx.compose.animation.core.AnimationSpec\))

## Add a Scaffold

Let's add the boilerplate for the `AppScaffold` and `ScreenScaffold` now.

Find "**`TODO (Start): Create a AppScaffold (Wear Version)`** " and add the code below it.

**Step 9**
    
    
    WearAppTheme {
    // TODO (Start): Create a AppScaffold (Wear Version)
    AppScaffold {
    

Find **`"TODO (Start): Create a ScreenScaffold (Wear Version)"`** and add the code below it.
    
    
    // TODO (Start): Create a ScreenScaffold (Wear Version)
    ScreenScaffold( 
        scrollState = listState,
        contentPadding = rememberResponsiveColumnPadding(
           first = ColumnItemType.IconButton,
           last = ColumnItemType.Button,
        ),
    ){contentPadding ->
    

Next, make sure you add the closing bracket to the right location.

Find **`"TODO (End): Create a ScreenScaffold (Wear Version)"`** and add the closing bracket there:

**Step 10**
    
    
    // TODO (End): Create a ScreenScaffold (Wear Version)
    }
    

Find **`"TODO (End): Create a AppScaffold (Wear Version)"`** and add the closing bracket there:

**Step 10**
    
    
    // TODO (End): Create a AppScaffold (Wear Version)
    }
    

Let's run it first. You should see something like this:

![97e417901b8f8229.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/97e417901b8f8229.png)

Notice that it adds:

  * A [`TimeText`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#TimeText\(androidx.compose.ui.Modifier,androidx.wear.compose.material.TimeSource,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1\)) which uses curved text under the hood and gives developers an easy way to show the time without placing the composable or having to do any work with time related classes. Additionally, the [Material Guidelines recommend that you display the time](https://developer.android.com/training/wearables/design/overlays#time) at the top of any screen within the app and it fades away while scrolling.
  * A [`ScrollIndicator`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScrollIndicator\(androidx.compose.foundation.lazy.LazyListState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.animation.core.AnimationSpec\)) which is an indicator on the right side of the screen to show the current indicator location based on the type of state object you pass in. In our case, that will be the [`TransformingLazyColumnState`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/TransformingLazyColumnState).



Ok, let's see what this looks like now:

![fd00c8fc4f7283ef.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/fd00c8fc4f7283ef.png)

Try scrolling it up and down. You should only see the scrolling indicator show up when you are scrolling.

## Add a Edge Hugging button

The [`EdgeButton`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/EdgeButton.composable#EdgeButton\(kotlin.Function0,androidx.compose.ui.Modifier,androidx.wear.compose.material3.EdgeButtonSize,kotlin.Boolean,androidx.wear.compose.material3.ButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1\)) is a new expressive button from the M3 Compose material for Wear OS release. The edge-hugging container is a new shape that embraces round and maximises the space within the circular form factor.

`ScreenScaffold` provides a slot for an EdgeButton that takes the available space below a scrolling list. It will scale up and fade in when the user scrolls to the end of the list, and scale down and fade out as the user scrolls up. Let's add an `EdgeButton` to our code:

**Step 11**
    
    
    ScreenScaffold(
      scrollState = listState,
      contentPadding = rememberResponsiveColumnPadding(
        first = ColumnItemType.IconButton,
        last = ColumnItemType.Button,
      ),
    /* *************************** Part 11: EdgeButton *************************** */
      // TODO: Add a EdgeButton
       edgeButton = {
         EdgeButton(
          onClick = { /* ... */ },
          buttonSize = EdgeButtonSize.Medium) {
            Text(stringResource(R.string.more))
          }
       }
    

You can specify [4 different sizes](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/EdgeButtonSize) for an `EdgeButton`: `ExtraSmall`, `Small`, `Medium` and `Large`.

Let's see what this looks like now:

![3a973bbfe4941e67.png](https://developer.android.com/static/codelabs/compose-for-wear-os/img/3a973bbfe4941e67.png)

Nice job, you have finished a UI demo of most of the Wear OS composables!

##  9\. Congratulations 

Congratulations! You learned the basics of using Compose on Wear OS!

Now you can reapply all your Compose knowledge to making beautiful Wear OS apps!

## What's next?

Check out the other Wear OS codelabs:

  * [Create your first Wear OS Tile](https://developer.android.com/codelabs/wear-tiles)



## Further reading

  * [Compose Starter sample](https://github.com/android/wear-os-samples/tree/main/ComposeStarter) on Github
  * [Build apps for the wrist with Wear OS](https://developer.android.com/wear) for more guides
  * [Use Jetpack Compose on Wear OS](https://developer.android.com/training/wearables/compose)



## Feedback

We'd love to hear from you about your experiences using Compose for Wear OS and what you are able to build! Join the discussion in the [Kotlin Slack](https://surveys.jetbrains.com/s3/kotlin-slack-sign-up) **#compose-wear** channel and keep providing feedback on the [issue tracker](https://issuetracker.google.com/issues/new?component=1077552&template=1598429).

Happy coding!

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
