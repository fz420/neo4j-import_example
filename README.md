# neo4j-admin import demo

## 目的

- 熟悉 neo4j-admin import 的数据格式要求
- 熟悉 neo4j-admin import 命令


## 命令

win10 下 neo4j desktop 本地新建数据库，测试导入成功。

```
C:\Users\admin\Documents\neo4j\relate-data\dbmss\dbms-8c126a77-e9ba-4f00-84b1-514a962b8f7b>.\bin\neo4j-admin.bat import --skip-bad-entries-logging=true --skip-duplicate-nodes=true --skip-bad-relationships=true
--id-type=INTEGER --nodes import\host_header.csv,import\host.csv --relationships import\relhost_header.csv,import\relhost.csv
Neo4j version: 4.2.1
Importing the contents of these files into C:\Users\admin\Documents\neo4j\relate-data\dbmss\dbms-8c126a77-e9ba-4f00-84b1-514a962b8f7b\data\databases\neo4j:
Nodes:
C:\Users\admin\Documents\neo4j\relate-data\dbmss\dbms-8c126a77-e9ba-4f00-84b1-514a962b8f7b\import\host_header.csv
C:\Users\admin\Documents\neo4j\relate-data\dbmss\dbms-8c126a77-e9ba-4f00-84b1-514a962b8f7b\import\host.csv

Relationships:
C:\Users\admin\Documents\neo4j\relate-data\dbmss\dbms-8c126a77-e9ba-4f00-84b1-514a962b8f7b\import\relhost_header.csv
C:\Users\admin\Documents\neo4j\relate-data\dbmss\dbms-8c126a77-e9ba-4f00-84b1-514a962b8f7b\import\relhost.csv

Available resources:
Total machine memory: 7.903GiB
Free machine memory: 2.333GiB
Max heap memory : 1.757GiB
Processors: 4
Configured max memory: 5.531GiB
High-IO: false

Import starting 2021-04-22 14:17:27.369+0800
Estimated number of nodes: 101.00
Estimated number of node properties: 303.00
Estimated number of relationships: 101.00
Estimated number of relationship properties: 0.00
Estimated disk space usage: 13.02KiB
Estimated required memory usage: 1020MiB

(1/4) Node import 2021-04-22 14:17:28.523+0800
Estimated number of nodes: 101.00
Estimated disk space usage: 9.666KiB
Estimated required memory usage: 1020MiB
-......... .......... .......... .......... .......... 5% ?266ms
.......... .......... .......... .......... .......... 10% ?10ms
.......... .......... .......... .......... .......... 15% ?5ms
.......... .......... .......... .......... .......... 20% ?4ms
.......... .......... .......... .......... .......... 25% ?9ms
.......... .......... .......... .......... .......... 30% ?6ms
.......... .......... .......... .......... .......... 35% ?4ms
.......... .......... .......... .......... .......... 40% ?6ms
.......... .......... .......... .......... .......... 45% ?4ms
.......... .......... .......... .......... .......... 50% ?3ms
.......... .......... .......... .......... .......... 55% ?7ms
.......... .......... .......... .......... .......... 60% ?6ms
.......... .......... .......... .......... .......... 65% ?5ms
.......... .......... .......... .......... .......... 70% ?3ms
.......... .......... .......... .......... .......... 75% ?4ms
.......... .......... .......... .......... .......... 80% ?3ms
.......... .......... .......... .......... .......... 85% ?4ms
.......... .......... .......... .......... .......... 90% ?4ms
.......... .......... .......... .......... .......... 95% ?5ms
.......... .......... .......... .......... .......... 100% ?3ms

(2/4) Relationship import 2021-04-22 14:17:29.126+0800
Estimated number of relationships: 101.00
Estimated disk space usage: 3.354KiB
Estimated required memory usage: 1.004GiB
.......... .......... .......... .......... .......... 5% ?800ms
.......... .......... .......... .......... .......... 10% ?7ms
.......... .......... .......... .......... .......... 15% ?4ms
.......... .......... .......... .......... .......... 20% ?3ms
.......... .......... .......... .......... .......... 25% ?3ms
.......... .......... .......... .......... .......... 30% ?3ms
.......... .......... .......... .......... .......... 35% ?4ms
.......... .......... .......... .......... .......... 40% ?4ms
.......... .......... .......... .......... .......... 45% ?2ms
.......... .......... .......... .......... .......... 50% ?3ms
.......... .......... .......... .......... .......... 55% ?5ms
.......... .......... .......... .......... .......... 60% ?2ms
.......... .......... .......... .......... .......... 65% ?4ms
.......... .......... .......... .......... .......... 70% ?3ms
.......... .......... .......... .......... .......... 75% ?3ms
.......... .......... .......... .......... .......... 80% ?5ms
.......... .......... .......... .......... .......... 85% ?4ms
.......... .......... .......... .......... .......... 90% ?3ms
.......... .......... .......... .......... .......... 95% ?2ms
.......... .......... .......... .......... .........(3/4) Relationship linking 2021-04-22 14:17:29.996+0800
Estimated required memory usage: 1020MiB
-......... .......... .......... .......... .......... 5% ?611ms
.......... .......... .......... .......... .......... 10% ?4ms
.......... .......... .......... .......... .......... 15% ?3ms
.......... .......... .......... .......... .......... 20% ?6ms
.......... .......... .......... .......... .......... 25% ?3ms
.......... .......... .......... .......... .......... 30% ?4ms
.......... .......... .......... .......... .......... 35% ?3ms
.......... .......... .......... .......... .......... 40% ?4ms
.......... .......... .......... .......... .......... 45% ?4ms
.......... .......... .......... .......... .......... 50% ?2ms
.......... .......... .......... .......... .......... 55% ?3ms
.......... .......... .......... .......... .......... 60% ?3ms
.......... .......... .......... .......... .......... 65% ?4ms
.......... .......... .......... .......... .......... 70% ?4ms
.......... .......... .......... .......... .......... 75% ?2ms
.......... .......... .......... .......... .......... 80% ?3ms
.......... .......... .......... .......... .......... 85% ?5ms
.......... .......... .......... .......... .......... 90% ?3ms
.......... .......... .......... .......... .......... 95% ?4ms
.......... .......... .......... .......... .......... 100% ?3ms

(4/4) Post processing 2021-04-22 14:17:30.959+0800
Estimated required memory usage: 1020MiB
-......... .......... .......... .......... .......... 5% ?983ms
.......... .......... .......... .......... .......... 10% ?4ms
.......... .......... .......... .......... .......... 15% ?2ms
.......... .......... .......... .......... .......... 20% ?2ms
.......... .......... .......... .......... .......... 25% ?3ms
.......... .......... .......... .......... .......... 30% ?3ms
.......... .......... .......... .......... .......... 35% ?4ms
.......... .......... .......... .......... .......... 40% ?3ms
.......... .......... .......... .......... .......... 45% ?3ms
.......... .......... .......... .......... .......... 50% ?4ms
.......... .......... .......... .......... .......... 55% ?3ms
.......... .......... .......... .......... .......... 60% ?4ms
.......... .......... .......... .......... .......... 65% ?3ms
.......... .......... .......... .......... .......... 70% ?4ms
.......... .......... .......... .......... .......... 75% ?4ms
.......... .......... .......... .......... .......... 80% ?2ms
.......... .......... .......... .......... .......... 85% ?3ms
.......... .......... .......... .......... .......... 90% ?3ms
.......... .......... .......... .......... .......... 95% ?3ms
.......... .......... .......... .......... .......... 100% ?4ms

IMPORT DONE in 6s 25ms.
Imported:
101 nodes
101 relationships
303 properties
Peak memory usage: 1.004GiB

C:\Users\admin\Documents\neo4j\relate-data\dbmss\dbms-8c126a77-e9ba-4f00-84b1-514a962b8f7b>


```
