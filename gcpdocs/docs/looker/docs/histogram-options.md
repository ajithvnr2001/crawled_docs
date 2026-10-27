---
url: https://docs.cloud.google.com/looker/docs/histogram-options/
title: Histogram chart options \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:36:52.384884+00:00
---

# Histogram chart options  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/histogram-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Histogram chart options Stay organized with collections  Save and categorize content based on your preferences. 

A histogram chart is a graphical representation of the data distribution of an attribute. A histogram creates intervals (bins) and counts how many values fall into each bin.

This page describes the options for editing histogram charts in the visualization menu. To use a histogram chart visualization, first select the **Histogram** option in the Explore **Visualization** bar. Next, select the **Edit** option on the visualization bar to edit your chart.

![](https://docs.cloud.google.com/static/looker/docs/images/histogram-chart-2618.png)

Some of the options that are listed on this documentation page may be unavailable (grayed out or hidden) when they conflict with other settings that you have chosen.

**Note:** Histogram charts have a maximum of 5,000 data points because of Looker's [row limits](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#row_limits).

## Plot menu options

### Visualization Theme

If your Looker admin has enabled the [**Modern User Interface** preview option](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#modern_user_interface), you will see the **Visualization Theme** option. This field lets you select between the **Modern** or **Classic** theme for the visualization. See [Using the modern user interface](https://docs.cloud.google.com/looker/docs/modern-ui) for more information.

### Series Positioning

You can specify how [series](https://docs.cloud.google.com/looker/docs/creating-visualizations#series-def) are clustered visually on a chart. Not all of the following options apply to all chart types:

  * **Grouped** : For column, and bar charts. Series are clustered side-by-side.
  * **Overlay** : For scatterplot, line, and area charts. Series are overlaid on the chart.
  * **Stacked** : Series values are added on the y-axis, so that each consecutive series appears above the last. Be sure that the units of all series match.
  * **Stacked Percentage** : Series values are presented as percentages stacked on the y-axis, where all values add up to between 99% and 101%. For additional precision, increase the **Value Format** decimal places.



### Field to Bin

Select the field that you want to use to create the histogram bins.

### Spacing

You can set the spacing between column groups. This parameter accepts values between 0 and 1. Enter 0 for minimum spacing between columns within a group. Enter 1 for maximum spacing.

### Bin Range Style

Specifies the format used for the bin labels on the x-axis. You can choose from the following styles:

  * **Interval** : Displays the range as `[x,y)`, which is inclusive of the bottom value and exclusive of the top value.
  * **Integer** : Displays the range as integers, such as `x to y`. This style is best suited for discrete integer values.
  * **Relational** : Displays the range using relational operators, such as `≥x and < y`.
  * **Hyphen** : Displays the range as `x - y`, which is inclusive of the bottom value and of the top value.



### Min Bound and Max Bound

Defines the minimum and maximum values of the data to be included in the bins.

  * **Min Bound** : Sets the lower limit for the bins. Any data with a value lower than this value may be excluded or grouped. Defaults to **Auto** based on the data.
  * **Max Bound** : Sets the upper limit for the bins. Any data with a value higher than this value may be excluded or grouped. Defaults to **Auto** based on the data.



### Number of Bins

Specifies the total number of bins (intervals) to create in the histogram.

  * By default, this is set to **Auto** , and the number of bins is calculated automatically based on the data distribution.
  * You can set a specific integer to suggest the chosen number of bins.



### Bin Width

Sets a specific numerical range (width) for each bin.

  * This option lets you control the granularity of the histogram by defining the size of each bucket.
  * **Note** : This setting takes precedence over **Number of Bins**. If you define a **Bin Width** value, the **Number of Bins** setting is ignored, and the number of bins is calculated automatically based on the specified width and the data range.



### Legend

You can toggle the appearance of the series legend on a chart. This option is available only when there is more than one series (except in the case of a pie chart).

### Legend Alignment

You can specify whether the series legend appears to the left, center, or right of the chart. This option is available only when **Hide Legend** is off and when there is more than one series.

### Limit Displayed Rows

You can show or hide rows in a visualization, based on their position in the results. For example, if your visualization displays a seven-day rolling average, you may want to hide the first six rows.

Click **Limit Displayed Rows** to enable or disable this feature. When this feature is enabled, you can specify the following options:

  * **Hide** or **Show** : Choose **Hide** to exclude certain rows from the visualization. Choose **Show** to display only a limited number of rows in the visualization.
  * **First** or **Last** : Choose if the rows to hide or show are the first or last rows in the result set.
  * **Number** : Specify the number of rows to hide or show.



In the Data section of the Look or Explore, excluded rows are shaded in a darker color.

![](https://docs.cloud.google.com/static/looker/docs/images/limit-displayed-rows-2106.png)

This option is dependent on the row order. Changing the query's sort order or adding a row limit can change the rows that are shown or hidden in the visualization.

### Edit Chart Config

The **Edit Chart Config** button at the bottom of the visualization menu opens the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/advanced-visualization-editor). This editor lets you modify [HighCharts](https://api.highcharts.com/highcharts/chart) visualizations by exposing certain JSON parameters of the visualization, enabling deep customization. These customizations will not dynamically interact with data.

The **Edit Chart Config** button is available if you have either the Looker [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) or the [`can_override_vis_config` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config).

See the [**Examples**](https://docs.cloud.google.com/looker/docs/advanced-visualization-editor#examples) section of the Chart Config Editor article for examples of some common use cases, including the following examples:

  * Changing the background color and axis text color
  * Conditional formatting of values within a series
  * Customizing tooltip color
  * Adding vertical reference bands and captions
  * Adding chart annotations



## Series menu options

The series menu controls how your chart shows each [data series](https://docs.cloud.google.com/looker/docs/creating-visualizations#series-def).

### Colors

You can define the color palette for a chart in the **Colors** section.

#### Collection

A collection lets you create themed visualizations and dashboards that look good together. All of Looker's built-in color collections appear on the [Color collections](https://docs.cloud.google.com/looker/docs/color-collections) documentation page. Your Looker admin may also create a custom color collection for your organization.

You can choose a color collection from the **Collection** drop-down menu. The **Palette** section will update with a palette from your chosen color collection.

#### Palette

Once you've selected a color collection, you can choose a different palette from the collection, or customize your palette, by clicking the color palette itself. This opens the palette picker and displays all of the palettes from the collection.

Colors are assigned to each series in order. For a [categorical palette](https://docs.cloud.google.com/looker/docs/color-collections), the first color in the palette is assigned to the first series, and so on. For a [sequential or diverging palette](https://docs.cloud.google.com/looker/docs/color-collections), the color at the left end of the palette is assigned to the first series and the colors for each remaining series move to the right on the palette. If your query returns more data series than colors listed, the colors repeat from the beginning of the palette, first as a lighter version of each color, then as a darker version of each color.

#### Creating a custom color palette

To create a custom color palette, select the **Custom** tab on the palette picker. You can edit your palette in several ways:

  * Click on one of the colors present to edit it.
  * Click the **+** or **-** buttons to add a color to the end of the palette or to remove a selected color.
  * Click **EDIT ALL** at the bottom right of the menu to use a comma-separated list of color values.



![](https://docs.cloud.google.com/static/looker/docs/images/color-palette-custom-2106.png)

To change a selected color, or edit all colors at once, input [hex strings](https://www.w3schools.com/colors/colors_hexadecimal.asp), such as `#2ca6cd`, or [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`, into the color value box at the bottom of the picker.

![](https://docs.cloud.google.com/static/looker/docs/images/color-hex-value-2106.png)

To bring up a color picker to select a color, click the color wheel to the right of the color value box. The corresponding hex value for that color appears in the color value box.

![](https://docs.cloud.google.com/static/looker/docs/images/color-picker-2106.png)

If you click **EDIT ALL** , the color value box populates with the hex codes of the color palette you've chosen or customized. Copying and pasting this list is the best way to copy custom color palettes from one chart to another.

#### Reverse colors

You can reverse the colors used on a palette. For a [categorical palette](https://docs.cloud.google.com/looker/docs/color-collections), this applies the last color in the palette to the first series, the second-to-last color in the palette to the second series, and so on. For a [sequential or diverging palette](https://docs.cloud.google.com/looker/docs/color-collections), this applies the color at the right end of the palette to the first series and move left on the palette for the remaining series.

### Show Full Field Name

You can determine whether to show the view name along with the field name for each axis title and series name. When **Show Full Field Name** is turned off, generally only the field name shows; however, measures of type `count` display only the view name instead.

### Customizations

You can customize each series in the chart in several ways:

![](https://docs.cloud.google.com/static/looker/docs/images/vis-customizations-line-area-2106.png)

  1. Click the arrow next to a series to expand its options.
  2. Click the color swatch to select a custom color for the series. This overrides the color palette that's defined by the **Colors** option.
  3. In the **Label** section, enter a custom series label. This optional label impacts the chart legend and tooltips.
  4. In the **Type** section, select a different visualization type for the series. This optional setting is useful to combine different visualization types on the same chart, such as showing one series as columns and another series as a line.
  5. In the **Points** section, for line, area, or scatter series types, select the shape of the chart points.
  6. Click the **Custom Tooltip** switch to configure tooltips within the [Explore visualization editor](https://docs.cloud.google.com/looker/docs/creating-visualizations#quick_guide) by using a combination of UI settings and an HTML editor that supports Liquid templating. [Learn more about custom tooltips](https://docs.cloud.google.com/looker/docs/custom-tooltips).

**Note:** Custom tooltips are not supported for [donut multiples charts](https://docs.cloud.google.com/looker/docs/donut-multiples-options), [word cloud charts](https://docs.cloud.google.com/looker/docs/word-cloud-options), [static map (regions) charts](https://docs.cloud.google.com/looker/docs/map-regions-options), [static maps (points) charts](https://docs.cloud.google.com/looker/docs/map-points-options), charts that are made using the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor) (with the exception of [Sankey charts](https://docs.cloud.google.com/looker/docs/sankey)), or custom visualizations.



## Values menu options

### Label Values

You can toggle the appearance of value labels for each data point on a chart.

### Value Colors

You can define the colors of the value labels. This field takes a comma-separated list of one or more color values. The color values can be formatted as RGB hex strings, such as `#2ca6cd`, or as [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`.

If set to multiple colors, colors are assigned to each series in order. The first series in the underlying table is assigned the first color, and so on. If the query returns more data series than colors listed, Looker will assign the series color to the value label after it runs out of your custom colors.

If no color values are provided, Looker assigns the series color to the value label.

### Font Size

You can set the font size of value labels using any valid [CSS size](https://developer.mozilla.org/en-US/Web/CSS/length). For example, you can specify a number of pixels, such as `10px` or `12px`.

### Value Format

You can specify the format of the value, independent of the underlying dimension or measure. The field accepts Excel-style formatting. If no formatting is specified, the value displays in the format of the underlying dimension or measure.

MS Excel's complete guide details how to specify these formats [in their documentation](https://support.office.com/en-us/article/review-guidelines-for-customizing-a-number-format-c0a1d1fa-d3f4-4018-96b7-9c9354dd99f5). However, color formatting is not currently supported in Looker.

> For Looker developers: The formatting used in the **Value Format** field is the same as formatting that is used with the [`value_format` LookML parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format), except that the `value_format` parameter requires the formatting string to be enclosed in double quotes. In the **Value Format** field, the formatting string is not enclosed in quotes.

The [Adding custom formatting to numeric fields](https://docs.cloud.google.com/looker/docs/custom-formatting#custom_formatting_examples) documentation page provides more information on how to use custom formatting.

### Totals Labels

You can toggle the appearance of totals labels for each data point on a chart. Totals labels are a sum of values. Totals count unique values only once.

### Totals Color

You can define the color of the totals labels. Click the color swatch to scroll through color palettes or select a custom color for the totals labels. **Totals Color** is only available when **Series Positioning** is set to Stacked.

### Totals Rotation

You can set the rotation of the totals labels. This parameter accepts values between -360 and 360, denoting the number of degrees to rotate the labels. **Totals Rotation** is only available with **Series Positioning** Stacked.

## X menu options

### Bin Label Format

Specifies the format used for the bin labels on the x-axis. You can choose from the following options:

  * **Single Value (x)** : Displays the bin labels as a single value at the same intervals across the x-axis.
  * **Interval (Inherit Bin Range Style)** : Displays the bin labels as a range in the same format as the **Bin Range Style** option.



### Reverse Axis

You can toggle the direction of the x-axis. When this is off, values increase from left to right. When this is on, values decrease from left to right.

### Allow Zoom

This option is available only for [Cartesian charts](https://docs.cloud.google.com/looker/docs/visualization-types#cartesian_charts) (column, bar, scatterplot, line, area, waterfall, or boxplot charts).

This option defaults to enabled. When it's enabled, you can zoom on a visualization in a dashboard, a Look, or an Explore.

See the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#zooming_on_cartesian_charts) or [Viewing Looks in Looker](https://docs.cloud.google.com/looker/docs/viewing-looks#zooming_on_cartesian_charts) documentation page for information about how to use the zoom feature.

When this option is disabled, the **Allow Zoom** option on the **Y** menu is hidden and you cannot zoom on the visualization.

### Show Axis Name

You can toggle the appearance of the x-axis name label.

### Custom Axis Name

You can set the name for the x-axis using any string value. This option is only available when **Show Axis Name** is ON.

### Show Axis Value Labels

**Axis Value Labels** toggles the appearance of value labels on the x-axis.

### Show Gridlines

You can toggle the appearance of gridlines extending from the x-axis. Gridlines are spaced based on the scaling of the x-axis.

### Value Format

You can specify the number format of the x-axis values, independent of the underlying dimension or measure. The parameter accepts Excel style formatting. If no formatting is specified, the value displays in the format of the underlying dimension or measure.

Excel's complete guide explains how to specify these formats [in the Excel documentation](https://support.microsoft.com/en-us/excel/review-guidelines-for-customizing-a-number-format). At this time, date formatting and color formatting are not supported in Looker.

Some of the most common formatting options are shown on the [Adding custom formatting to numeric fields](https://docs.cloud.google.com/looker/docs/custom-formatting) documentation page.

### Label Rotation

You can set the rotation of the x-axis value labels. This parameter accepts values between -360 and 360, denoting the number of degrees to rotate the labels.

## Y menu options

### Display Mode

Specifies how the y-axis values are calculated and displayed. You can choose from the following options:

  * **Count** : Displays the raw frequency, which is the count of records that fall within each bin.
  * **Percent of Total** : Displays the density, which is the percentage of total records that fall within each bin. This option is useful for comparing distributions across different datasets or categories.



### Show Gridlines

You can toggle the appearance of gridlines extending from the y-axis. Gridlines are spaced based on the scaling of the y-axis.

### Reverse Axes

You can toggle the direction of the y-axis. When off, values increase going up the axis. When on, values decrease going up the axis.

### Allow Zoom

This option is available only for [Cartesian charts](https://docs.cloud.google.com/looker/docs/visualization-types#cartesian_charts) (column, bar, scatterplot, line, area, waterfall, or boxplot charts).

This option is available only when the **Allow Zoom** option on the **X** menu is enabled. This option defaults to enabled. When it's enabled, you can zoom on a visualization in a dashboard, a Look, or an Explore.

See the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#zooming_on_cartesian_charts) or [Viewing Looks](https://docs.cloud.google.com/looker/docs/viewing-looks#zooming_on_cartesian_charts) documentation page for information about how to use the zoom feature.

If this option is disabled but the **Allow Zoom** option on the **X** menu is enabled, you cannot zoom into a tighter view of the y-axis; you can zoom only into a tighter view of the x-axis.

### Configure Axis

The **Configure Axis** section includes options to configure the y-axis in the **Left Axis** section.

### Scale Type

You can specify how the y-axis scale is calculated and displayed. _Not all of the following options apply to all chart types._

  * **Linear** : Data is plotted along the y-axis as evenly spaced, discrete entries, regardless of relative distance between data points. This is the default setting. Most data is best displayed on a linear scale.

  * **Logarithmic** : Data is plotted along the y-axis using a logarithmic scale, which is based on orders of magnitude. If the data has a cluster of very small and very large values, this setting lets you see variation in the small values while also showing the larger values. The logarithmic scale type can only be used for data with positive values and is only available when you have set **Series Positioning** to **Grouped** or **Overlay** on the **Plot** tab.




### Show Axis Name

You can toggle the appearance of y-axis name labels.

### Axis Name

You can enter the label for the selected y-axis.

### Show Axis Value Labels

You can toggle the appearance of y-axis values.

### Y Axis Format

You can specify the number format of the y-axis values, independent of the underlying dimension or measure. The parameter accepts Excel style formatting. If no formatting is specified, the value displays in the format of the underlying dimension or measure.

Excel's complete guide explains how to specify these formats [in the Excel documentation](https://support.office.com/en-us/article/review-guidelines-for-customizing-a-number-format-c0a1d1fa-d3f4-4018-96b7-9c9354dd99f5). At this time, date formatting and color formatting are not supported in Looker.

Some of the most common formatting options are shown on the [Adding custom formatting to numeric fields](https://docs.cloud.google.com/looker/docs/custom-formatting) documentation page.

### Min Value

You can define the minimum value for the selected y-axis.

### Max Value

You can define the maximum value for the selected y-axis.

### Unpin Axis

You can toggle the chart focus on the area for which data exists, rather than showing the full scale starting at zero.

### Tick Density

You can set the density of tick marks on the y-axis as follows:

  * **Default** : Sets ticks to the default density.

  * **Custom** : Set ticks with a custom density. A slider bar lets you set the custom density.




### Add Reference Line

Reference lines are applied to the first series in your query results and ignore any hidden series. You can reorder the columns in the data table to change the series the reference line is applied to.

The **Add Reference Line** button enables the creation of reference lines in a chart. Click it as many times as you like to add any number of reference lines and reveal the settings for those reference lines. To delete a reference line, click the **X** in the upper right of its settings.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
