---
url: https://docs.cloud.google.com/bigtable/docs/hbase-differences/
title: Differences between HBase and Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:59:59.979918+00:00
---

# Differences between HBase and Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Differences between HBase and Bigtable

One way to access Bigtable is to use a customized version of the Apache HBase client for Java. In general, the customized client exposes the [same API](https://hbase.apache.org/apidocs/) as a standard installation of HBase. This page describes the differences between the Cloud Bigtable HBase client for Java and a standard HBase installation. Many of these difference are related to management tasks that Bigtable handles automatically.

The Cloud Bigtable HBase client for Java is for customers who are migrating to Bigtable from HBase and want to continue using the HBase API. In all other cases, Java developers should instead use the [Cloud Bigtable client for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), which calls the Bigtable APIs. 

## Column families

When you create a column family, you cannot configure the block size or compression method, either with the HBase shell or through the HBase API. Bigtable manages the block size and compression for you.

In addition, if you use the HBase shell to get information about a table, the HBase shell will always report that each column family does not use compression. In reality, Bigtable uses proprietary compression methods for all of your data.

The following column family settings are ignored, because Bigtable manages the underlying storage for you:

  * `BLOCKCACHE`
  * `BLOCKSIZE`
  * `BLOOMFILTER`
  * `CACHE_BLOOMS_ON_WRITE`
  * `CACHE_DATA_IN_L1`
  * `CACHE_DATA_ON_WRITE`
  * `CACHE_INDEX_ON_WRITE`
  * `COMPRESS_TAGS`
  * `COMPRESSION`
  * `COMPRESSION_COMPACT`
  * `DATA_BLOCK_ENCODING`
  * `EVICT_BLOCKS_ON_CLOSE`
  * `IN_MEMORY`
  * `KEEP_DELETED_CELLS`
  * `PREFETCH_BLOCKS_ON_OPEN`
  * `REPLICATION_SCOPE`



The settings `VERSIONS`, `MIN_VERSIONS`, and `TTL` are converted to Bigtable [garbage collection policies](https://docs.cloud.google.com/bigtable/docs/garbage-collection).

Bigtable requires that column family names follow the regular expression `[_a-zA-Z0-9][-_.a-zA-Z0-9]*`. If you are importing data into Bigtable from HBase, you might need to first change the family names to follow this pattern.

## Rows and cells

  * You cannot define an ACL for an individual row. Bigtable [authorized views](https://docs.cloud.google.com/bigtable/docs/authorized-views) let you grant access to a subset of a table's data, but they aren't exposed through the HBase API.
  * You cannot set the visibility of individual cells.
  * Tags are not supported. You cannot use the class [`org.apache.hadoop.hbase.Tag`](https://hbase.apache.org/devapidocs/org/apache/hadoop/hbase/Tag.html) to add metadata to individual cells. Any tags that you add to a cell are dropped before the cell is written.



## Mutations and deletions

  * [`Append`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Append.html) operations in Bigtable are fully atomic for both readers and writers. Readers will never be able to read a partially applied `Append` operation.
  * [`Increment`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Increment.html) operations are atomic, but setting a time range on an `Increment` is not supported.
  * A [`RowMutations`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/RowMutations.html) object that you pass to `Table#mutateRow()` can contain either `Put` and `Delete` operations or `Append` and `Increment` operations, but not both. `RowMutations` objects that contain `Append` or `Increment` operations aren't supported in `batch()`, `checkAndMutate()`, or `BufferedMutator`.
  * Deleting a specific version of a specific column based on its timestamp is supported. However, the following types of deletions are not supported:

    * Deleting only the latest version of a column
    * Deleting all values in a row that have a specific timestamp
    * Deleting all values in a column family at or before a specific timestamp

As a result, the following methods in the class [`org.apache.hadoop.hbase.client.Delete`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Delete.html) are not supported: \+ `new Delete(byte[] row, long timestamp)` \+ `addColumn(byte[] family, byte[] qualifier)` \+ `addFamily(byte[] family, long timestamp)` \+ `addFamilyVersion(byte[] family, long timestamp)`

  * In HBase, [deletes mask puts](http://hbase.apache.org/book.html#_deletes_mask_puts), but Bigtable does not mask puts after deletes when put requests are sent after deletion requests. This means that in Bigtable, a write request sent to a cell is not affected by a previously sent delete request to the same cell.




## Gets and scans

  * Reverse scans let you read a range of rows backwards. For details, see [Reverse scans](https://docs.cloud.google.com/bigtable/docs/reads#reverse-scan).
  * Unlike HBase, when you send a read request, Bigtable doesn't automatically filter out expired data that is marked for deletion in an upcoming garbage collection cycle. To avoid reading expired data, use a filter in the read request. For more information, see the [Garbage collection overview](https://docs.cloud.google.com/bigtable/docs/garbage-collection).
  * Limiting the number of values per row per column family is not supported. You cannot call the method [`org.apache.hadoop.hbase.client.Scan#setMaxResultsPerColumnFamily(int limit)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setMaxResultsPerColumnFamily-int-).
  * Partial results aren't supported. Rows are always returned whole. Calls to the methods [`org.apache.hadoop.hbase.client.Scan#setBatch(int batch)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setBatch-int-) and [`org.apache.hadoop.hbase.client.Scan#setAllowPartialResults(boolean allowPartialResults)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setAllowPartialResults-boolean-) are ignored.
  * On a synchronous `Table#getScanner(Scan)` call, [`org.apache.hadoop.hbase.client.Scan#setCaching(int caching)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setCaching-int-) controls how many rows the client fetches at a time. `AsyncTable#getScanner()` ignores `setCaching()`. Calls to the method [`org.apache.hadoop.hbase.client.Scan#setMaxResultSize(long maxResultSize)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setMaxResultSize-long-) are always ignored.



## Coprocessors

Coprocessors are not supported. You cannot create classes that implement the interface [`org.apache.hadoop.hbase.coprocessor`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/coprocessor/package-summary.html).

## Filters

The following table lists the supported filters in the package [`org.apache.hadoop.hbase.filter`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/filter/package-summary.html). All other filters in that package aren't supported and throw an `UnsupportedOperationException`.

Supported | Supported, with limitations  
---|---  
  
  1. `PrefixFilter` scans for rows in the `PrefixFilter` in most cases. However, if `PrefixFilter` is part of a `FilterList` and has the operator `MUST_PASS_ONE`, Bigtable cannot determine the implied range and instead performs an unfiltered scan from the start row to the stop row. Use `PrefixFilter` with `BigtableExtendedScan` or a combination of filters to optimize performance in this case. 
  2. Requires a single column family only when you use a column qualifier as the column offset. 
  3. Supports only a single column family. 
  4. Supports only the `EQUAL` operator, with either the `BinaryComparator` comparator or the `RegexStringComparator` comparator. 
  5. Constructing the filter with `new KeyOnlyFilter(true)` is not supported. 
  6. Can't be part of a `FilterList` that uses the `MUST_PASS_ONE` operator. 
  7. A `PageFilter` must be the top-level filter or the last filter in a top-level `FilterList` that uses the `MUST_PASS_ALL` operator, which is the default behavior. A `PageFilter` in a `FilterList` that uses the `MUST_PASS_ONE` operator is not supported. 
  8. Supports only the `BinaryComparator` comparator, or the `RegexStringComparator` comparator with the `EQUAL` operator. If any operator other than `EQUAL` is used, only a single column family is supported. 
  9. Supports only the following comparators: 
     * `BinaryComparator`
     * `RegexStringComparator` with no flags (flags are ignored) and the `EQUAL` operator 
  10. Relies on the Bigtable condition filter, which can be slow. Supported but not recommended. 
  11. Only one `WhileMatchFilter` is supported per scan. 

  
`ColumnCountGetFilter`  
`ColumnPrefixFilter`  
`FilterList`  
`FirstKeyOnlyFilter`  
`FuzzyRowFilter`  
`MultipleColumnPrefixFilter`  
`PrefixFilter` 1  
`RandomRowFilter`  
`TimestampsFilter` |  `ColumnPaginationFilter` 2  
`ColumnRangeFilter` 3  
`FamilyFilter` 4  
`KeyOnlyFilter` 5  
`MultiRowRangeFilter` 6  
`PageFilter` 7  
`QualifierFilter` 8  
`RowFilter` 4  
`SingleColumnValueExcludeFilter` 3, 9, 10  
`SingleColumnValueFilter` 9, 10  
`ValueFilter` 9  
`WhileMatchFilter` 6, 11  
  
In addition, the following differences affect Bigtable filters:

  * Only the comparators `BinaryComparator` and `RegexStringComparator` are supported. All other comparators aren't supported and throw an `UnsupportedOperationException`.
  * In filters that use the regular expression comparator (`org.apache.hadoop.hbase.filter.RegexStringComparator`), regular expressions use [RE2 syntax](https://github.com/google/re2/wiki/Syntax), not Java syntax.
  * Custom filters are not supported. You cannot create classes that inherit from [`org.apache.hadoop.hbase.filter.Filter`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/filter/Filter.html). To use a Bigtable filter that has no HBase equivalent, wrap it in a `com.google.cloud.bigtable.hbase.filter.BigtableFilter`.
  * There is a size limit of 20 KB on filter expressions, and filters can't be nested more than 20 levels deep. As a workaround to reduce the size of a filter expression, use a supplementary column that stores the hash value of the filter criteria.



## Timestamps

Bigtable stores timestamps in microseconds, while HBase stores timestamps in milliseconds. This distinction has implications when you use the HBase client library for Bigtable and you have data with reversed timestamps.

The client library converts between microseconds and milliseconds, but because that the largest HBase timestamp that Bigtable can store is Long.MAX_VALUE/1000, any value larger than that is converted to Long.MAX_VALUE/1000. As a result, large reversed timestamp values might not convert correctly.

## Administration

This section describes how the Bigtable HBase client for Java implements the [`org.apache.hadoop.hbase.client.Admin`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Admin.html) interface. Because Bigtable handles most cluster and storage management tasks automatically, many HBase administrative methods aren't applicable. Any `Admin` method that isn't listed in this section as supported or as having no effect isn't supported and throws an `UnsupportedOperationException`.

### Table management

The following `Admin` methods for managing tables and column families are supported:

  * `addColumnFamily(TableName tableName, ColumnFamilyDescriptor columnFamily)` and `addColumnFamilyAsync(TableName tableName, ColumnFamilyDescriptor columnFamily)` (HBase 1.x: `addColumn(TableName tableName, HColumnDescriptor column)`)
  * `createTable(TableDescriptor desc)`, `createTable(TableDescriptor desc, byte[][] splitKeys)`, `createTable(TableDescriptor desc, byte[] startKey, byte[] endKey, int numRegions)`, `createTableAsync(TableDescriptor desc)`, and `createTableAsync(TableDescriptor desc, byte[][] splitKeys)`
  * `deleteColumnFamily(TableName tableName, byte[] columnName)` and `deleteColumnFamilyAsync(TableName tableName, byte[] columnName)` (HBase 1.x: `deleteColumn(TableName tableName, byte[] columnName)`)
  * `deleteTable(TableName tableName)`, `deleteTableAsync(TableName tableName)`, `deleteTables(Pattern pattern)`, and `deleteTables(String regex)`
  * `disableTable(TableName tableName)`, `disableTableAsync(TableName tableName)`, `disableTables(Pattern pattern)`, and `disableTables(String regex)`
  * `enableTable(TableName tableName)`, `enableTableAsync(TableName tableName)`, `enableTables(Pattern pattern)`, and `enableTables(String regex)`
  * `getAlterStatus(TableName tableName)` and `getAlterStatus(byte[] tableName)`
  * `getDescriptor(TableName tableName)`, `getTableDescriptor(TableName tableName)`, `getTableDescriptors(List<String> names)`, and `getTableDescriptorsByTableName(List<TableName> tableNames)`
  * `isTableAvailable(TableName tableName)` and `isTableAvailable(TableName tableName, byte[][] splitKeys)`
  * `isTableDisabled(TableName tableName)` and `isTableEnabled(TableName tableName)`
  * `listTableDescriptors()`, `listTableDescriptors(List<TableName> tableNames)`, `listTableDescriptors(Pattern pattern)`, and `listTableDescriptors(Pattern pattern, boolean includeSysTables)` (HBase 1.x: `listTables()`, `listTables(Pattern pattern)`, `listTables(Pattern pattern, boolean includeSysTables)`, `listTables(String regex)`, and `listTables(String regex, boolean includeSysTables)`)
  * `listTableNames()`, `listTableNames(Pattern pattern)`, `listTableNames(Pattern pattern, boolean includeSysTables)`, `listTableNames(String regex)`, and `listTableNames(String regex, boolean includeSysTables)`
  * `modifyColumnFamily(TableName tableName, ColumnFamilyDescriptor columnFamily)` and `modifyColumnFamilyAsync(TableName tableName, ColumnFamilyDescriptor columnFamily)` (HBase 1.x: `modifyColumn(TableName tableName, HColumnDescriptor column)`)
  * `modifyTable(TableDescriptor td)`, `modifyTable(TableName tableName, TableDescriptor td)`, `modifyTableAsync(TableDescriptor td)`, and `modifyTableAsync(TableName tableName, TableDescriptor td)`
  * `tableExists(TableName tableName)`
  * `truncateTable(TableName tableName, boolean preserveSplits)` and `truncateTableAsync(TableName tableName, boolean preserveSplits)`



The following supported table management methods behave differently on Bigtable or ignore certain parameters:

  * Bigtable tables can't be disabled. `disableTable()`, `disableTableAsync()`, `disableTables()`, `enableTable()`, `enableTableAsync()`, and `enableTables()` change the state of the table only in the client's memory (which `isTableDisabled()` and `isTableEnabled()` read).
  * `modifyTable()` and `modifyTableAsync()` apply only changes to column families. Table-level attributes are ignored.
  * `truncateTable()` and `truncateTableAsync()` delete all of the data in the table. The `preserveSplits` parameter is ignored.
  * `listTableDescriptors()`, `listTables()`, and `listTableNames()` overloads that accept an `includeSysTables` parameter ignore `includeSysTables`, because Bigtable doesn't have system tables.
  * `isTableAvailable(TableName tableName, byte[][] splitKeys)` checks only whether the table exists and ignores the `splitKeys` parameter.
  * `getAlterStatus()` always returns `(0, 0)` because schema modifications in Bigtable are synchronous.



Tasks such as table compaction and splitting are handled automatically. As a result, the following methods have no effect:

  * `compact(TableName tableName)`
  * `compact(TableName tableName, byte[] columnFamily)`
  * `majorCompact(TableName tableName)`
  * `majorCompact(TableName tableName, byte[] columnFamily)`
  * `split(TableName tableName)`
  * `split(TableName tableName, byte[] splitPoint)`



### Snapshots

HBase snapshot methods create and manage Bigtable [backups](https://docs.cloud.google.com/bigtable/docs/backups). Because backups are stored in a specific cluster, if your instance has more than one cluster, you must set the configuration property `google.bigtable.snapshot.cluster.id` to the cluster to use. Backups that you create with `snapshot()` expire after the number of seconds in the configuration property `google.bigtable.snapshot.default.ttl.secs` (24 hours by default). `cloneSnapshot()` restores from a backup to a new table.

The following snapshot methods are supported in `Admin`:

  * `cloneSnapshot(byte[] snapshotName, TableName tableName)`
  * `cloneSnapshot(String snapshotName, TableName tableName)`
  * `deleteSnapshot(byte[] snapshotName)`
  * `deleteSnapshot(String snapshotName)`
  * `snapshot(byte[] snapshotName, TableName tableName)`
  * `snapshot(String snapshotName, TableName tableName)`



In addition, `AsyncAdmin` supports `listSnapshots()`, `listSnapshots(Pattern pattern)`, and `snapshot(SnapshotDescription snapshot)`. All other snapshot methods—including `restoreSnapshot()`, `deleteSnapshots()`, `deleteTableSnapshots()`, `listTableSnapshots()`, and `cloneSnapshot(String snapshotName, TableName tableName, boolean restoreAcl)`—aren't supported and throw an `UnsupportedOperationException`.

### Region management

Bigtable uses tablets, which are similar to regions. The following methods for retrieving region information are supported, with differences from standard HBase:

  * `getRegions(TableName tableName)` and `getTableRegions(TableName tableName)`, as well as the methods in the interface [`org.apache.hadoop.hbase.client.RegionLocator`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/RegionLocator.html), return approximate boundaries based on a sample of row keys in the table. The server names in the returned regions aren't real servers.
  * `getRegionMetrics(ServerName serverName, TableName tableName)` ignores the `serverName` parameter and returns approximate region size metrics based on a sample of row keys in the table.



Because Bigtable manages your tablets automatically, the following methods have no effect:

  * `assign(byte[] regionName)`
  * `compactRegion(byte[] regionName)`
  * `compactRegion(byte[] regionName, byte[] columnFamily)`
  * `flushRegion(byte[] regionName)`
  * `majorCompactRegion(byte[] regionName)`
  * `majorCompactRegion(byte[] regionName, byte[] columnFamily)`
  * `splitRegion(byte[] regionName)`
  * `splitRegion(byte[] regionName, byte[] splitPoint)`



In HBase 1.x, `compactRegionServer(ServerName sn, boolean major)`, `mergeRegions(byte[] encodedNameOfRegionA, byte[] encodedNameOfRegionB, boolean forcible)`, `move(byte[] encodedRegionName, byte[] destServerName)`, and `unassign(byte[] regionName, boolean force)` also have no effect. Their HBase 2.x equivalents aren't supported and throw an `UnsupportedOperationException`.

### Cluster status and connection

Bigtable handles cluster maintenance tasks automatically, so maintenance methods in `Admin` throw an `UnsupportedOperationException`. Only the following connection and status methods are supported:

  * `close()` has no effect.
  * `getClusterMetrics()`, `getClusterMetrics(EnumSet<Option> options)`, and `getClusterStatus()` return placeholder values with empty server lists, and `getClusterMetrics(EnumSet<Option> options)` ignores the `options` parameter.
  * `getConfiguration()` returns the client `Configuration` object.
  * `getConnection()` returns the client `Connection` object.



### Namespaces

Bigtable does not use namespaces. You can [use row key prefixes to simulate namespaces](https://docs.cloud.google.com/bigtable/docs/schema-design#multitenancy).

By default, all namespace methods throw an `UnsupportedOperationException`. However, if you set the configuration property `google.bigtable.namespace.warnings` to `true`, the following methods log a warning and have no effect (returning `null` or an empty result) instead of throwing an exception:

  * `createNamespace(NamespaceDescriptor descriptor)`
  * `deleteNamespace(String name)`
  * `deleteNamespaceAsync(String name)`
  * `getNamespaceDescriptor(String name)`
  * `listNamespaceDescriptors()`
  * `listTableDescriptorsByNamespace(byte[] name)`
  * `listTableDescriptorsByNamespace(String name)`
  * `listTableNamesByNamespace(String name)`
  * `modifyNamespace(NamespaceDescriptor descriptor)`



Even when `google.bigtable.namespace.warnings` is set to `true`, `listNamespaces()` throws an `UnsupportedOperationException`.

### Other administrative features

Bigtable doesn't support `Admin` methods in the following categories, and calling them throws an `UnsupportedOperationException`:

  * **Locality groups** : Bigtable doesn't let you specify locality groups for column families.
  * **Coprocessors and distributed procedures** : Bigtable doesn't support coprocessors or distributed procedures.
  * **Quotas** : To learn about Bigtable quotas, see [Quotas and limits](https://docs.cloud.google.com/bigtable/quotas).
  * **Replication** : Bigtable replicates data automatically between the clusters in an instance. For details, see [Replication overview](https://docs.cloud.google.com/bigtable/docs/replication-overview). To replicate from HBase to Bigtable, see [Replicate from HBase to Bigtable](https://docs.cloud.google.com/bigtable/docs/hbase-replication).
  * **Access control** : Bigtable uses [IAM](https://docs.cloud.google.com/bigtable/docs/access-control) for access control.
  * **RegionServer groups** : Bigtable manages servers automatically and doesn't expose RegionServer groups.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
