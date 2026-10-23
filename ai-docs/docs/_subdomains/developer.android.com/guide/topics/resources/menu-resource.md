---
url: https://developer.android.com/guide/topics/resources/menu-resource/
title: Menu resource \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:36.489193+00:00
---

# Menu resource  |  Views  |  Android Developers

> Source: https://developer.android.com/guide/topics/resources/menu-resource/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



#  Menu resource Stay organized with collections  Save and categorize content based on your preferences. 

A menu resource defines an application menu—an options menu, context menu, or submenu—that can be inflated with `[MenuInflater](https://developer.android.com/reference/android/view/MenuInflater)`.

For a guide to using menus, see [Add menus](https://developer.android.com/guide/topics/ui/menus).

file location:
    `res/menu/_filename_.xml`  
The filename is used as the resource ID
compiled resource datatype:
    Resource pointer to a `[Menu](https://developer.android.com/reference/android/view/Menu)` (or subclass) resource
resource reference:
     In Java: `R.menu._filename_`  
In XML: `@[_package_ :]menu._filename_`
syntax:
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <menu xmlns:android="http://schemas.android.com/apk/res/android">
        <item android:id="@[+][_package_ :]id/_resource_name_ "
              android:title="_string_ "
              android:titleCondensed="_string_ "
              android:icon="@[package:]drawable/_drawable_resource_name_ "
              android:onClick="_method name_"
              android:showAsAction=["ifRoom" | "never" | "withText" | "always" | "collapseActionView"]
              android:actionLayout="@[package:]layout/_layout_resource_name_ "
              android:actionViewClass="_class name_"
              android:actionProviderClass="_class name_"
              android:alphabeticShortcut="_string_ "
              android:alphabeticModifiers=["META" | "CTRL" | "ALT" | "SHIFT" | "SYM" | "FUNCTION"]
              android:numericShortcut="_string_ "
              android:numericModifiers=["META" | "CTRL" | "ALT" | "SHIFT" | "SYM" | "FUNCTION"]
              android:checkable=["true" | "false"]
              android:visible=["true" | "false"]
              android:enabled=["true" | "false"]
              android:menuCategory=["container" | "system" | "secondary" | "alternative"]
              android:orderInCategory="_integer_ " />
        <group android:id="@[+][_package_ :]id/_resource name_"
               android:checkableBehavior=["none" | "all" | "single"]
               android:visible=["true" | "false"]
               android:enabled=["true" | "false"]
               android:menuCategory=["container" | "system" | "secondary" | "alternative"]
               android:orderInCategory="_integer_ " >
            <item />
        </group>
        <item >
            <menu>
              <item />
            </menu>
        </item>
    </menu>

elements:
    

`<menu>`
    **Required.** This must be the root node. Contains `<item>` and/or `<group>` elements. 

Attributes:

`xmlns:android`
    _XML namespace_. **Required.** Defines the XML namespace, which must be `"http://schemas.android.com/apk/res/android"`. 
`<item>`
    A menu item. Might contain a `<menu>` element (for a submenu). Must be a child of a `<menu>` or `<group>` element. 

Attributes:

`android:id`
    _Resource ID_. A unique resource ID. To create a new resource ID for this item, use the form: `"@+id/_name_ "`. The plus symbol indicates that this is created as a new ID.
`android:title`
    _String resource_. The menu title as a string resource or raw string.
`android:titleCondensed`
    _String resource_. A condensed title as a string resource or a raw string. This title is used for situations in which the normal title is too long.
`android:icon`
    _Drawable resource_. An image to be used as the menu item icon.
`android:onClick`
    _Method name_. The method to call when this menu item is clicked. The method must be declared in the activity as public. It accepts a `[MenuItem](https://developer.android.com/reference/android/view/MenuItem)` as its only parameter, which indicates the item clicked. This method takes precedence over the standard callback to `[onOptionsItemSelected()](https://developer.android.com/reference/android/app/Activity#onOptionsItemSelected\(android.view.MenuItem\))`. See the example at the end of this page. 

**Warning:** If you obfuscate your code using [ProGuard](https://developer.android.com/tools/help/proguard) or a similar tool, be sure to exclude the method you specify in this attribute from renaming, because it can break the functionality.

Introduced in API level 11.

`android:showAsAction`
    _Keyword_. When and how this item appears as an action item in the app bar. A menu item can appear as an action item only when the activity includes an app bar. Valid values: Value| Description  
---|---  
`ifRoom`| Only place this item in the app bar if there is room for it. If there isn't room for all the items marked `"ifRoom"`, the items with the lowest `orderInCategory` values are displayed as actions, and the remaining items are displayed in the overflow menu.  
`withText`| Also include the title text (defined by `android:title`) with the action item. You can include this value along with one of the others as a flag set by separating them with a pipe `|`.  
`never`| Never place this item in the app bar. Instead, list the item in the app bar's overflow menu.  
`always`| Always place this item in the app bar. Avoid using this unless it's critical that the item always appear in the action bar. Setting multiple items to always appear as action items can result in them overlapping with other UI in the app bar.  
`collapseActionView`| The action view associated with this action item (as declared by `android:actionLayout` or `android:actionViewClass`) is collapsible.  
Introduced in API level 14.  
  
See [Add the app bar](https://developer.android.com/training/appbar) for more information.

Introduced in API level 11.

`android:actionLayout`
    _Layout resource_. A layout to use as the action view. 

For more information, see [Use action views and action providers](https://developer.android.com/training/appbar/action-views).

Introduced in API level 11.

`android:actionViewClass`
    _Class name_. A fully-qualified class name for the `[View](https://developer.android.com/reference/android/view/View)` to use as the action view. For example, `"android.widget.SearchView"` to use `[SearchView](https://developer.android.com/reference/android/widget/SearchView)` as an action view. 

For more information, see [Use action views and action providers](https://developer.android.com/training/appbar/action-views).

**Warning:** If you obfuscate your code using [ProGuard](https://developer.android.com/tools/help/proguard) or a similar tool, be sure to exclude the class you specify in this attribute from renaming, because it can break the functionality.

Introduced in API level 11.

`android:actionProviderClass`
    _Class name_. A fully qualified class name for the `[ActionProvider](https://developer.android.com/reference/android/view/ActionProvider)` to use in place of the action item. For example, `"android.widget.ShareActionProvider"` to use `[ShareActionProvider](https://developer.android.com/reference/android/widget/ShareActionProvider)`. 

For more information, see [Use action views and action providers](https://developer.android.com/training/appbar/action-views).

**Warning:** If you obfuscate your code using [ProGuard](https://developer.android.com/tools/help/proguard) or a similar tool, be sure to exclude the class you specify in this attribute from renaming, because it can break the functionality.

Introduced in API level 14.

`android:alphabeticShortcut`
    _Char_. A character for the alphabetic shortcut key.
`android:numericShortcut`
    _Integer_. A number for the numeric shortcut key.
`android:alphabeticModifiers`
    _Keyword_. A modifier for the menu item's alphabetic shortcut. The default value corresponds to the `Control` key. Valid values: Value| Description  
---|---  
`META` | Corresponds to the `Meta` meta key.  
`CTRL` | Corresponds to the `Control` meta key.  
`ALT` | Corresponds to the `Alt` meta key.  
`SHIFT` | Corresponds to the `Shift` meta key.  
`SYM` | Corresponds to the `Sym` meta key.  
`FUNCTION` | Corresponds to the `Function` meta key.  
  
**Note** : You can specify multiple keywords in an attribute. For example, `android:alphabeticModifiers="CTRL|SHIFT"` indicates that to trigger the corresponding menu item, the user needs to press both the `Control` and `Shift` meta keys along with the shortcut.

You can use the `setAlphabeticShortcut()` method to set the attribute values programmatically. For more information about the `alphabeticModifier` attribute, see `[alphabeticModifiers](https://developer.android.com/reference/android/R.attr#alphabeticModifiers)`.

`android:numericModifiers`
    _Keyword_. A modifier for the menu item's numeric shortcut. The default value corresponds to the `Control` key. Valid values: Value| Description  
---|---  
`META` | Corresponds to the `Meta` meta key.  
`CTRL` | Corresponds to the `Control` meta key.  
`ALT` | Corresponds to the `Alt` meta key.  
`SHIFT` | Corresponds to the `Shift` meta key.  
`SYM` | Corresponds to the `Sym` meta key.  
`FUNCTION` | Corresponds to the `Function` meta key.  
  
**Note** : You can specify multiple keywords in an attribute. For example, `android:numericModifiers="CTRL|SHIFT"` indicates that to trigger the corresponding menu item, the user needs to press both the `Control` and `Shift` meta keys along with the shortcut.

You can use the `setNumericShortcut()` method to set the attribute values programmatically. For more information about the `numericModifier` attribute, see `[numericModifiers](https://developer.android.com/reference/android/R.attr#numericModifiers)`.

`android:checkable`
    _Boolean_. True if the item is checkable.
`android:checked`
    _Boolean_. True if the item is checked by default.
`android:visible`
    _Boolean_. True if the item is visible by default.
`android:enabled`
    _Boolean_. True if the item is enabled by default.
`android:menuCategory`
    _Keyword_. Value corresponding to the `[Menu](https://developer.android.com/reference/android/view/Menu)` `CATEGORY_*` constants, which define the item's priority. Valid values: Value| Description  
---|---  
`container`| For items that are part of a container.  
`system`| For items that are provided by the system.  
`secondary`| For items that are user-supplied secondary (infrequently used) options.  
`alternative`| For items that are alternative actions on the data that is currently displayed.  
`android:orderInCategory`
    _Integer_. The order of importance of the item within a group.
`<group>`
    A menu group, to create a collection of items that share traits, such as whether they are visible, enabled, or selectable. Contains one or more `<item>` elements. Must be a child of a `<menu>` element. 

Attributes:

`android:id`
    _Resource ID_. A unique resource ID. To create a new resource ID for this item, use the form: `"@+id/_name_ "`. The plus symbol indicates that this is created as a new ID.
`android:checkableBehavior`
    _Keyword_. The type of selectable behavior for the group. Valid values: Value| Description  
---|---  
`none`| Not selectable.  
`all`| All items can be selected (use checkboxes).  
`single`| Only one item can be selected (use radio buttons).  
`android:visible`
    _Boolean_. True if the group is visible.
`android:enabled`
    _Boolean_. True if the group is enabled.
`android:menuCategory`
    _Keyword_. Value corresponding to the `[Menu](https://developer.android.com/reference/android/view/Menu)` `CATEGORY_*` constants, which define the group's priority. Valid values: Value| Description  
---|---  
`container`| For groups that are part of a container.  
`system`| For groups that are provided by the system.  
`secondary`| For groups that are user-supplied secondary (infrequently used) options.  
`alternative`| For groups that are alternative actions on the data that is currently displayed.  
`android:orderInCategory`
    _Integer_. The default order of the items within the category.
example:
    XML file saved at `res/menu/example_menu.xml`: 
    
    
    <menu xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto">
        <item android:id="@+id/item1"
              android:title="@string/item1"
              android:icon="@drawable/group_item1_icon"
              app:showAsAction="ifRoom|withText"/>
        <group android:id="@+id/group">
            <item android:id="@+id/group_item1"
                  android:onClick="onGroupItemClick"
                  android:title="@string/group_item1"
                  android:icon="@drawable/group_item1_icon" />
            <item android:id="@+id/group_item2"
                  android:onClick="onGroupItemClick"
                  android:title="@string/group_item2"
                  android:icon="@drawable/group_item2_icon" />
        </group>
        <item android:id="@+id/submenu"
              android:title="@string/submenu_title"
              app:showAsAction="ifRoom|withText" >
            <menu>
                <item android:id="@+id/submenu_item1"
                      android:title="@string/submenu_item1" />
            </menu>
        </item>
    </menu>

The following application code inflates the menu from the `[onCreateOptionsMenu(Menu)](https://developer.android.com/reference/android/app/Activity#onCreateOptionsMenu\(android.view.Menu\))` callback and also declares the on-click callback for two of the items:

### Kotlin
    
    
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.example_menu, menu)
        return true
    }
    
    fun onGroupItemClick(item: MenuItem) {
        // One of the group items (using the onClick attribute) was clicked.
        // The item parameter passed here indicates which item it is.
        // All other menu item clicks are handled by Activity.onOptionsItemSelected.
    }

### Java
    
    
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.example_menu, menu);
        return true;
    }
    
    public void onGroupItemClick(MenuItem item) {
        // One of the group items (using the onClick attribute) was clicked.
        // The item parameter passed here indicates which item it is.
        // All other menu item clicks are handled by Activity.onOptionsItemSelected.
    }

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
