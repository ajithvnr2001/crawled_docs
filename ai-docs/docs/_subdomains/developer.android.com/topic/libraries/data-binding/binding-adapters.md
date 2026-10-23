---
url: https://developer.android.com/topic/libraries/data-binding/binding-adapters/
title: Binding adapters \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:24.459364+00:00
---

# Binding adapters  |  Views  |  Android Developers

> Source: https://developer.android.com/topic/libraries/data-binding/binding-adapters/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



#  Binding adapters Stay organized with collections  Save and categorize content based on your preferences. 

Binding adapters are responsible for making the appropriate framework calls to set values. One example is setting a property value, like calling the [`setText()`](https://developer.android.com/reference/android/widget/TextView#setText\(int\)) method. Another example is setting an event listener, like calling the [`setOnClickListener()`](https://developer.android.com/reference/android/view/View#setOnClickListener\(android.view.View.OnClickListener\)) method.

The Data Binding Library lets you specify the method called to set a value, provide your own binding logic, and specify the type of the returned object by using adapters.

## Set attribute values

Whenever a bound value changes, the generated binding class must call a setter method on the view with the binding expression. You can let the Data Binding Library automatically determine the method, or you can explicitly declare the method or provide custom logic to select a method.

### Automatic method selection

For an attribute named `example`, the library automatically finds the method `setExample(arg)` that accepts compatible types as the argument. The namespace of the attribute isn't considered. Only the attribute name and type are used when searching for a method.

For example, given the `android:text="@{user.name}"` expression, the library looks for a `setText(arg)` method that accepts the type returned by `user.getName()`. If the return type of `user.getName()` is `String`, the library looks for a `setText()` method that accepts a `String` argument. If the expression returns an `int`, the library searches for a `setText()` method that accepts an `int` argument. The expression must return the correct type. You can cast the return value if necessary.

Data binding works even if no attribute exists with the given name. You can create attributes for any setter by using data binding. For example, the support class [`DrawerLayout`](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout) doesn't have attributes, but it has plenty of setters. The following layout automatically uses the [`setScrimColor(int)`](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout#setScrimColor\(int\)) and [`addDrawerListener(DrawerListener)`](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout#addDrawerListener\(androidx.drawerlayout.widget.DrawerLayout.DrawerListener\)) methods as the setter for the `app:scrimColor` and `app:drawerListener` attributes, respectively:
    
    
    <androidx.drawerlayout.widget.DrawerLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:scrimColor="@{@color/scrim}"
        app:drawerListener="@{fragment.drawerListener}">
    

### Specify a custom method name

Some attributes have setters that don't match by name. In these situations, an attribute can be associated with the setter using the [`BindingMethods`](https://developer.android.com/reference/androidx/databinding/BindingMethods) annotation. The annotation is used with a class and can contain multiple [`BindingMethod`](https://developer.android.com/reference/androidx/databinding/BindingMethod) annotations, one for each renamed method. Binding methods are annotations that you can add to any class in your app.

In the following example, the `android:tint` attribute is associated with the [`setImageTintList(ColorStateList)`](https://developer.android.com/reference/android/widget/ImageView#setImageTintList\(android.content.res.ColorStateList\)) method—not with the `setTint()` method:

### Kotlin
    
    
    @BindingMethods(value = [
        BindingMethod(
            type = android.widget.ImageView::class,
            attribute = "android:tint",
            method = "setImageTintList")])

### Java
    
    
    @BindingMethods({
           @BindingMethod(type = "android.widget.ImageView",
                          attribute = "android:tint",
                          method = "setImageTintList"),
    })

Typically, you don't need to rename setters in Android framework classes. The attributes are already implemented using the name convention to automatically find matching methods.

### Provide custom logic

Some attributes need custom binding logic. For example, there is no associated setter for the `android:paddingLeft` attribute. Instead, the `setPadding(left, top, right, bottom)` method is provided. A static binding adapter method with the [`BindingAdapter`](https://developer.android.com/reference/androidx/databinding/BindingAdapter) annotation lets you customize how a setter for an attribute is called.

The attributes of the Android framework classes already have `BindingAdapter` annotations. The following example shows the binding adapter for the `paddingLeft` attribute:

### Kotlin
    
    
    @BindingAdapter("android:paddingLeft")
    fun setPaddingLeft(view: View, padding: Int) {
        view.setPadding(padding,
                    view.getPaddingTop(),
                    view.getPaddingRight(),
                    view.getPaddingBottom())
    }

### Java
    
    
    @BindingAdapter("android:paddingLeft")
    public static void setPaddingLeft(View view, int padding) {
      view.setPadding(padding,
                      view.getPaddingTop(),
                      view.getPaddingRight(),
                      view.getPaddingBottom());
    }

The parameter types are important. The first parameter determines the type of the view that is associated with the attribute. The second parameter determines the type accepted in the binding expression for the given attribute.

Binding adapters are also useful for other types of customization. For example, a custom loader can be called from a worker thread to load an image.

You can also have adapters that receive multiple attributes, as shown in the following example:

### Kotlin
    
    
    @BindingAdapter("imageUrl", "error")
    fun loadImage(view: ImageView, url: String, error: Drawable) {
        Picasso.get().load(url).error(error).into(view)
    }

### Java
    
    
    @BindingAdapter({"imageUrl", "error"})
    public static void loadImage(ImageView view, String url, Drawable error) {
      Picasso.get().load(url).error(error).into(view);
    }

You can use the adapter in your layout, as shown in the following example. Note that `@drawable/venueError` refers to a resource in your app. Surrounding the resource with `@{}` makes it a valid binding expression.
    
    
    <ImageView app:imageUrl="@{venue.imageUrl}" app:error="@{@drawable/venueError}" />
    

**Note:** The Data Binding Library ignores custom namespaces for matching purposes.

The adapter is called if `imageUrl` and `error` are used for an [`ImageView`](https://developer.android.com/reference/android/widget/ImageView) object, `imageUrl` is a string, and `error` is a [`Drawable`](https://developer.android.com/reference/android/graphics/drawable/Drawable). If you want the adapter to be called when any of the attributes are set, set the optional [`requireAll`](https://developer.android.com/reference/androidx/databinding/BindingAdapter#requireAll\(\)) flag of the adapter to `false`, as shown in the following example:

### Kotlin
    
    
    @BindingAdapter(value = ["imageUrl", "placeholder"], requireAll = false)
    fun setImageUrl(imageView: ImageView, url: String?, placeHolder: Drawable?) {
        if (url == null) {
            imageView.setImageDrawable(placeholder);
        } else {
            MyImageLoader.loadInto(imageView, url, placeholder);
        }
    }

### Java
    
    
    @BindingAdapter(value={"imageUrl", "placeholder"}, requireAll=false)
    public static void setImageUrl(ImageView imageView, String url, Drawable placeHolder) {
      if (url == null) {
        imageView.setImageDrawable(placeholder);
      } else {
        MyImageLoader.loadInto(imageView, url, placeholder);
      }
    }

**Note:** Your binding adapters override the default data binding adapters when there is a conflict.

Binding adapter methods can take the old values in their handlers. A method taking old and new values must declare all old values for the attributes first, followed by the new values, as shown in the following example:

### Kotlin
    
    
    @BindingAdapter("android:paddingLeft")
    fun setPaddingLeft(view: View, oldPadding: Int, newPadding: Int) {
        if (oldPadding != newPadding) {
            view.setPadding(newPadding,
                        view.getPaddingTop(),
                        view.getPaddingRight(),
                        view.getPaddingBottom())
        }
    }

### Java
    
    
    @BindingAdapter("android:paddingLeft")
    public static void setPaddingLeft(View view, int oldPadding, int newPadding) {
      if (oldPadding != newPadding) {
          view.setPadding(newPadding,
                          view.getPaddingTop(),
                          view.getPaddingRight(),
                          view.getPaddingBottom());
       }
    }

Event handlers can only be used with interfaces or abstract classes with one abstract method, as shown in the following example:

### Kotlin
    
    
    @BindingAdapter("android:onLayoutChange")
    fun setOnLayoutChangeListener(
            view: View,
            oldValue: View.OnLayoutChangeListener?,
            newValue: View.OnLayoutChangeListener?
    ) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            if (oldValue != null) {
                view.removeOnLayoutChangeListener(oldValue)
            }
            if (newValue != null) {
                view.addOnLayoutChangeListener(newValue)
            }
        }
    }

### Java
    
    
    @BindingAdapter("android:onLayoutChange")
    public static void setOnLayoutChangeListener(View view, View.OnLayoutChangeListener oldValue,
           View.OnLayoutChangeListener newValue) {
      if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        if (oldValue != null) {
          view.removeOnLayoutChangeListener(oldValue);
        }
        if (newValue != null) {
          view.addOnLayoutChangeListener(newValue);
        }
      }
    }

Use this event handler in your layout as follows:
    
    
    <View android:onLayoutChange="@{() -> handler.layoutChanged()}"/>
    

When a listener has multiple methods, it must be split into multiple listeners. For example, [`View.OnAttachStateChangeListener`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener) has two methods: [`onViewAttachedToWindow(View)`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener#onViewAttachedToWindow\(android.view.View\)) and [`onViewDetachedFromWindow(View)`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener#onViewDetachedFromWindow\(android.view.View\)). The library provides two interfaces to differentiate the attributes and handlers for them:

### Kotlin
    
    
    // Translation from provided interfaces in Java:
    @TargetApi(Build.VERSION_CODES.HONEYCOMB_MR1)
    interface OnViewDetachedFromWindow {
        fun onViewDetachedFromWindow(v: View)
    }
    
    @TargetApi(Build.VERSION_CODES.HONEYCOMB_MR1)
    interface OnViewAttachedToWindow {
        fun onViewAttachedToWindow(v: View)
    }

### Java
    
    
    @TargetApi(VERSION_CODES.HONEYCOMB_MR1)
    public interface OnViewDetachedFromWindow {
      void onViewDetachedFromWindow(View v);
    }
    
    @TargetApi(VERSION_CODES.HONEYCOMB_MR1)
    public interface OnViewAttachedToWindow {
      void onViewAttachedToWindow(View v);
    }

Because changing one listener can affect the other, you need an adapter that works for either attribute or for both. You can set `requireAll` to `false` in the annotation to specify that not every attribute must be assigned a binding expression, as shown in the following example:

### Kotlin
    
    
    @BindingAdapter(
            "android:onViewDetachedFromWindow",
            "android:onViewAttachedToWindow",
            requireAll = false
    )
    fun setListener(view: View, detach: OnViewDetachedFromWindow?, attach: OnViewAttachedToWindow?) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR1) {
            val newListener: View.OnAttachStateChangeListener?
            newListener = if (detach == null && attach == null) {
                null
            } else {
                object : View.OnAttachStateChangeListener {
                    override fun onViewAttachedToWindow(v: View) {
                        attach.onViewAttachedToWindow(v)
                    }
    
                    override fun onViewDetachedFromWindow(v: View) {
                        detach.onViewDetachedFromWindow(v)
                    }
                }
            }
    
            val oldListener: View.OnAttachStateChangeListener? =
                    ListenerUtil.trackListener(view, newListener, R.id.onAttachStateChangeListener)
            if (oldListener != null) {
                view.removeOnAttachStateChangeListener(oldListener)
            }
            if (newListener != null) {
                view.addOnAttachStateChangeListener(newListener)
            }
        }
    }

### Java
    
    
    @BindingAdapter({"android:onViewDetachedFromWindow", "android:onViewAttachedToWindow"}, requireAll=false)
    public static void setListener(View view, OnViewDetachedFromWindow detach, OnViewAttachedToWindow attach) {
        if (VERSION.SDK_INT >= VERSION_CODES.HONEYCOMB_MR1) {
            OnAttachStateChangeListener newListener;
            if (detach == null && attach == null) {
                newListener = null;
            } else {
                newListener = new OnAttachStateChangeListener() {
                    @Override
                    public void onViewAttachedToWindow(View v) {
                        if (attach != null) {
                            attach.onViewAttachedToWindow(v);
                        }
                    }
                    @Override
                    public void onViewDetachedFromWindow(View v) {
                        if (detach != null) {
                            detach.onViewDetachedFromWindow(v);
                        }
                    }
                };
            }
    
            OnAttachStateChangeListener oldListener = ListenerUtil.trackListener(view, newListener,
                    R.id.onAttachStateChangeListener);
            if (oldListener != null) {
                view.removeOnAttachStateChangeListener(oldListener);
            }
            if (newListener != null) {
                view.addOnAttachStateChangeListener(newListener);
            }
        }
    }

The above example is slightly complicated because the [`View`](https://developer.android.com/reference/android/view/View) class uses the [`addOnAttachStateChangeListener()`](https://developer.android.com/reference/android/view/View#addOnAttachStateChangeListener\(android.view.View.OnAttachStateChangeListener\)) and [`removeOnAttachStateChangeListener()`](https://developer.android.com/reference/android/view/View#removeOnAttachStateChangeListener\(android.view.View.OnAttachStateChangeListener\)) methods instead of a setter method for [`OnAttachStateChangeListener`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener). The `android.databinding.adapters.ListenerUtil` class helps keep track of these listeners so that they can be removed in the binding adapter.

## Object conversions

### Automatic object conversion

When an [`Object`](https://developer.android.com/reference/java/lang/Object) is returned from a binding expression, the library selects the method used to set the value of the property. The `Object` is cast to a parameter type of the chosen method. This behavior is convenient in apps using the [`ObservableMap`](https://developer.android.com/reference/androidx/databinding/ObservableMap) class to store data, as shown in the following example:
    
    
    <TextView
       android:text='@{userMap["lastName"]}'
       android:layout_width="wrap_content"
       android:layout_height="wrap_content" />
    

**Note:** You can also refer to a value in the map using the `object.key` notation. For example, you can replace `@{userMap["lastName"]}` in the previous example with `@{userMap.lastName}`.

The `userMap` object in the expression returns a value, which is automatically cast to the parameter type found in the `setText(CharSequence)` method used to set the value of the `android:text` attribute. If the parameter type is ambiguous, cast the return type in the expression.

### Custom conversions

In some situations, a custom conversion is required between specific types. For example, the `android:background` attribute of a view expects a `Drawable`, but the `color` value specified is an integer. The following example shows an attribute that expects a `Drawable`, but an integer is provided instead:
    
    
    <View
       android:background="@{isError ? @color/red : @color/white}"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"/>
    

Whenever a `Drawable` is expected and an integer is returned, convert the `int` to a [`ColorDrawable`](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable). To perform the conversion, use a static method with a [`BindingConversion`](https://developer.android.com/reference/androidx/databinding/BindingConversion) annotation, as follows:

### Kotlin
    
    
    @BindingConversion
    fun convertColorToDrawable(color: Int) = ColorDrawable(color)

### Java
    
    
    @BindingConversion
    public static ColorDrawable convertColorToDrawable(int color) {
        return new ColorDrawable(color);
    }

However, the value types provided in the binding expression must be consistent. You can't use different types in the same expression, as shown in the following example:
    
    
    // The @drawable and @color represent different value types in the same
    // expression, which causes a build error.
    <View
       android:background="@{isError ? @drawable/error : @color/white}"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"/>
    

## Additional resources

To learn more about data binding, see the following resources.

### Samples

  * [Android Data Binding Library samples](https://github.com/android/databinding-samples)



### Codelabs

  * [Data Binding in Android](https://codelabs.developers.google.com/codelabs/android-databinding)



### Blog posts

  * [Data Binding — lessons learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Data Binding Library](https://developer.android.com/topic/libraries/data-binding)
  * [Layouts and binding expressions](https://developer.android.com/topic/libraries/data-binding/expressions)
  * [View binding](https://developer.android.com/topic/libraries/view-binding)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 

  * [ ![X](https://developer.android.com/_static/android/images/logo-x.svg) X  ](https://x.com/AndroidDev)

Follow @AndroidDev on X

  * [ ![YouTube](https://www.gstatic.com/images/icons/material/product/2x/youtube_48dp.png) YouTube  ](https://www.youtube.com/user/androiddevelopers)

Check out Android Developers on YouTube

  * [ ![LinkedIn](https://developer.android.com/_static/android/images/logo-linkedin.svg) LinkedIn  ](https://www.linkedin.com/showcase/androiddev)

Connect with the Android Developers community on LinkedIn




  * ### More Android

    * [ Android ](https://www.android.com)
    * [ Android for Enterprise ](https://www.android.com/enterprise/)
    * [ Security ](https://www.android.com/security-center/)
    * [ Source ](https://source.android.com)
    * [ News ](https://developer.android.com/news)
    * [ Blog ](https://android-developers.googleblog.com/)
    * [ Podcasts ](https://developer.android.com/podcasts)
  * ### Discover

    * [ Gaming ](https://developer.android.com/games)
    * [ Machine Learning ](https://developer.android.com/ml)
    * [ Health & Fitness ](https://developer.android.com/health-and-fitness)
    * [ Camera & Media ](https://developer.android.com/media)
    * [ Privacy ](https://developer.android.com/privacy)
    * [ 5G ](https://developer.android.com/training/connectivity/5g)
  * ### Android Devices

    * [ Large screens ](https://developer.android.com/large-screens)
    * [ Wear OS ](https://developer.android.com/wear)
    * [ ChromeOS devices ](https://developer.android.com/chrome-os)
    * [ Android for cars ](https://developer.android.com/cars)
    * [ Android TV ](https://developer.android.com/tv)
  * ### Releases

    * [ Android 17 ](https://developer.android.com/about/versions/17)
    * [ Android 16 ](https://developer.android.com/about/versions/16)
    * [ Android 15 ](https://developer.android.com/about/versions/15)
    * [ Android 14 ](https://developer.android.com/about/versions/14)
    * [ Android 13 ](https://developer.android.com/about/versions/13)
    * [ Android 12 ](https://developer.android.com/about/versions/12)
    * [ Android 11 ](https://developer.android.com/about/versions/11)
  * ### Documentation and Downloads

    * [ Android Studio guide ](https://developer.android.com/studio/intro)
    * [ Developers guides ](https://developer.android.com/guide)
    * [ API reference ](https://developer.android.com/reference)
    * [ Download Studio ](https://developer.android.com/studio)
    * [ Android NDK ](https://developer.android.com/ndk)
  * ### Support

    * [ Report platform bug ](https://issuetracker.google.com/issues/new?component=190923&template=841312)
    * [ Report documentation bug ](https://issuetracker.google.com/issues/new?component=192697)
    * [ Google Play support ](https://support.google.com/googleplay/android-developer)
    * [ Join research studies ](https://g.co/userresearch/androiddeveloperfooter)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/android/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com)
  * [ Chrome ](https://developer.chrome.com/home)
  * [ Firebase ](https://firebase.google.com)
  * [ Google Cloud Platform ](https://cloud.google.com)
  * [ All products ](https://developers.google.com/products/)



  * [ Privacy ](https://policies.google.com/privacy)
  * [ License ](https://developer.android.com/license)
  * [ Brand guidelines ](https://developer.android.com/distribute/marketing-tools/brand-guidelines)
  * Manage cookies 
  * Get news and tips by email [ Subscribe ](https://developer.android.com/updates)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


