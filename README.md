## Elastic Search, AWS, Python 을 활용한 코로나 시대에 따른 서울시 문화 시설 추천
### Data analysis based on 2014 Seoul Metro flow data & 2020 Current Status of Cultural Facilities Data

Writer : **[Sumin Woo](mailto:wsm9764@naver.com)**, E-Business, Ajou Univ.


| **Covid-19, Where do you enjoy your culture life?** <br/> : Recommend a safe place in Seoul-si | Flow Chart |
| ------ | ------ |
| <img width="1024" alt="demo" src="https://user-images.githubusercontent.com/51018265/100545565-c4ed3180-329f-11eb-9e31-62d2adaefddb.png"> | <img width="1024" alt="flow" src="https://user-images.githubusercontent.com/51018265/100545568-c7e82200-329f-11eb-92ba-0e9fdbb95ea3.png"> | 

| Metric : Normalized Data & Harmonic Mean  | Recomendation |
| ------ | ------ |
| <img width="1024" alt="Metric" src="https://user-images.githubusercontent.com/51018265/100545863-7d67a500-32a1-11eb-93b5-11a6b8351028.png"> | <img width="1024" alt="recommendation" src="https://user-images.githubusercontent.com/51018265/100545860-78a2f100-32a1-11eb-83be-79bd0241fbe7.png"> |




## Related Technology
<img width="96" alt="aws-logo" src="https://user-images.githubusercontent.com/75171481/100520150-afb0ce00-31df-11eb-9fe0-51ac2e41b91e.png"> <img width="96" alt="elk-logo" src="https://user-images.githubusercontent.com/75171481/100520151-b0496480-31df-11eb-9bdd-f1682cca1076.png"><img width="128" alt="py-logo" src="https://user-images.githubusercontent.com/75171481/100520236-1b933680-31e0-11eb-85fe-194854e61b25.png">


## Dashboard
| Total Seoul-metro-2014 | Cultural Facilities-2020 at Each Station|
| ------ | ------ |
| <img width="512" alt="seoul-metro-demo" src="https://user-images.githubusercontent.com/75171481/100519947-82175500-31de-11eb-8827-9eb92a65f060.png"> | <img width="512" alt="Cultural Facilities Data" src="https://user-images.githubusercontent.com/75171481/100519979-abd07c00-31de-11eb-9e0d-b9c21494b897.png"> | 

|  Seoul-metro-2014 Weekend Flow Order | Cultural Facilities-2020|
| ------ | ------ |
|<img width="512" alt="seoul-metro-demo" src="https://user-images.githubusercontent.com/75171481/100519984-b0953000-31de-11eb-8667-3293891d2b10.png">|<img width="512" alt="seoul-metro-demo" src="https://user-images.githubusercontent.com/75171481/100519986-b559e400-31de-11eb-90d0-6a87ed7e2ad0.png">|

|  Weekend Flow Data for station having many culture facilities | Weekday Flow Data for station having many culture facilities|
| ------ | ------ |
|<img width="512" alt="Weekend" src="https://user-images.githubusercontent.com/75171481/100546042-7ee59d00-32a2-11eb-9576-cf272c31ae2b.png">|<img width="512" alt="Weekday" src="https://user-images.githubusercontent.com/75171481/100546043-8147f700-32a2-11eb-8219-9e698d5a87f2.png">|

## Getting started
### Install dependencies

#### How to start AWS
- ``` Excute Elastic Search and Kibana background on server If you want AWS. ```
- ``` Excute logstach and filebeat for uploading data on your local If server memory is full. ```
- ```It is explained in detail in the link below.```

[AWS EC2 Guide](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/concepts.html)

#### Main Requirements

- npm install
- Python
- tmux
- [elastic search](https://www.elastic.co/kr/downloads/elasticsearch)
- [kibana](https://www.elastic.co/kr/downloads/kibana)
- [logstash](https://www.elastic.co/kr/downloads/logstash)
- [filebeat](https://www.elastic.co/kr/downloads/beats/filebeat)
- ```./bin/kibana plugin --install elastic/sense```

#### ETC Requirements

- ```pip install -r requirements.txt```

## Raw Data Link
- [2015 - 2019 raw Total Seoul Metro Data](https://data.seoul.go.kr/dataList/OA-12921/F/1/datasetView.do)
- [2020 raw Cultural Facilities Data](http://data.seoul.go.kr/dataList/OA-151/S/1/datasetView.do;jsessionid=4D71BA84EE5A2C7480DFBD7A979BD455.new_portal-svr-11)

## Preprocessd Data Link
- [2014 Total Seoul Metro Data](https://drive.google.com/file/d/0ByqsUCpttxAGd1VXRU41VmJBNWs)
- [2014 Seoul Metro Weekday Data except start_time](https://drive.google.com/file/d/1uKPY5Y4dYwSERF7CUdcdTCi5zXzzfVyU/view?usp=sharing)
- [2014 Seoul Metro Weekend Data](https://drive.google.com/file/d/1qsholyoYg6K9q7omwjHIA_aVsuSrAhwX/view?usp=sharing)
- [2020 Current Status of Cultural Facilities Data](https://drive.google.com/file/d/1uuVDKVuK93GsfBdaUShZbq6_HUC2pJHl/view?usp=sharing)

## How to preprocess Data from Raw using Python

</div>
</details>

<details>
<summary> Details (If you want details click here!) </summary>
<div markdown="1">
 </div>
</details>


## How to execute Elasticsearch & Kibana 
- ```tmux new -s elk, tmux attach -t elk``` (for keep server in background processing)
- ```bin/elasticsearch``` 
- ```(ctrl + b) -> d``` (for escaping tmux)
- repeat above process about kibana
- ```tmux new -s kibaba, tmux attach -t kibana```
- ```bin/kibana```

## How to set elasticsearch with above data

###  ▶ 1. 2014 Seoul Metro Data

#### elasticsearch

- index name: seoul-metro-2014
- type: seoul-metro
- mapping info:

field | type | description
---- | ---- | ----
time_slot | datetime | 승/하차 시간. 1시간 단위.
line_num | string | 호선 (1호선, 2호선 ...)
line_num_en | string | 호선(영문) (Line 1, Line 2 ...)
station_name | string | 역 이름 : 잠실
station_name | string | 역 이름 전체 : 잠실(송파구청)
station_name | string | 역 이름 영문
station_name | string | 역 이름 한자
station_name | string | 역 이름 중국어 간체
station_name | string | 역 이름 일본어
station_geo { lat , lon } | geo_point | 역 좌표
people_in | integer | 승차인원
people_out | integer | 하차인원


- PUT mapping information to kibana sense like below

```
PUT /seoul-metro-2014'
  {
    "mappings" : {
      "seoul-metro" : {
        "properties" : {
          "time_slot" : { "type" : "date" },
          "line_num" : { "type" : "string", "index" : "not_analyzed" },
          "line_num_en" : { "type" : "string", "index" : "not_analyzed" },
          "station_name" : { "type" : "string", "index" : "not_analyzed" },
          "station_name_kr" : { "type" : "string", "index" : "not_analyzed" },
          "station_name_en" : { "type" : "string", "index" : "not_analyzed" },
          "station_name_chc" : { "type" : "string", "index" : "not_analyzed" },
          "station_name_ch" : { "type" : "string", "index" : "not_analyzed" },
          "station_name_jp" : { "type" : "string", "index" : "not_analyzed" },
          "station_geo" : { "type" : "geo_point" },
          "people_in" : { "type" : "integer" },
          "people_out" : { "type" : "integer" }
        }
      }
    }
  }'
```

#### logstash

- ```cd logstash/```
- ```vim logstash.conf in terminal, and then write like below```

- logstash.conf:

```
input {
  file {
    codec => json
    port => 5044
  }
}

filter{
  mutate {
    remove_field => [ "@version", "@timestamp", "host", "path" ]
  }
}

output{
  elasticsearch{
    hosts => ["127.0.0.1"]
    index => "seoul-metro-2014"
    document_type => "seoul-metro"
  }
}
```

#### filebeat

- ```cd filebeat/```
- ```vim filebeat.yml```
- ```set the log path```
- ```change enabled flag (false -> true)```
- ```comment output.elasticsearch and host (because we use logstash)```
- ```write host: [127.0.0.1:5044] in output.logstash```
```
enabled: true
paths:
  - <your path>/data/*.log

#output.elasticsearch:
#hosts: ["localhost:9200"]

output.logstash:
   hosts: ["127.0.0.1:5044"]
```

### ▶ 2. 2020 Current Status of Cultural Facilities Data

#### elasticsearch

- index name: seoul-metro-culture-facilities
- type: seoul-culture
- mapping info:

field | type | description
---- | ---- | ----
station_name | string | 역 이름
library | integer | 도서관 수
museum | integer | 박물관 수
culture_center | integer | 문화 센터 수
art_gallery | integer | 미술관 수
stadium | integer | 공연장 수
arts_center | integer | 미술 센터 수
etc | integer | 기타 문화시설 수
total_sum | integer | 해당 역 문화시설 전체 합
station_geo { lat , lon } | geo_point | 역 좌표


- ```PUT mapping information to kibana sense like below```

```
PUT /seoul-metro-culture-facilities
  {
    "mappings" : {
      "seoul-metro" : {
        "properties" : {
          "station_name" : { "type" : "string", "index" : "not_analyzed" },
          "library" : { "type" : integer },
          "museum" : { "type" : integer },
          "culture_center" : { "type" : integer },
          "art_gallery" : { "type" : integer },
          "stadium" : { "type" : integer },
          "arts_center" : { "type" : integer },
          "etc" : { "type" : integer },
          "total_sum" : { "type" : integer },
          "station_geo" : { "type" : "geo_point" }
        }
      }
    }
  }
```

#### logstash

- ```cd logstash/```
- ```vim logstash.conf in terminal, and then change index "seoul-metro-2014" to "seoul-metro-culture-facilities"```

#### filebeat

- ```cd filebeat/```
- ```vim filebeat.yml```
- ```change the log path for seoul-metro-culture-facilities```

## How to execute logstash & filebeat
- ```tmux new -s logs, tmux attach -t logs``` (for keep server in background processing)
- ```bin/logstash -f logstash.conf``` 
- ```(ctrl + b) -> d``` (for escaping tmux)

- **```./filebeat -c filebeat.yml```*** 
- **And Check whether your data is uploaded to Your Elastic Server!**

## Reference
- [Seoul Metro Data Analysis with Elasticsearch](https://github.com/kimjmin/elastic-demo)
