# 무중단 배포 - In djago
https://gist.github.com/majackson/493c3d6d4476914ca9da63f84247407b
https://blog.myungseokang.dev/posts/online-schema-change/
https://www.shayon.dev/post/2022/47/pg-osc-zero-downtime-schema-changes-in-postgresql/


# DTO, DAO, VO 







# 샤딩, 파티셔닝 테이블, view
# database_practice

## 몽고 DB 공부 제대로

https://meetup.toast.com/posts/274


https://lazygyu.net/blog/hype_driven_development


https://github.com/KimDoKy/study/blob/book/book/WebEnginnerNoTameNoDataBase/ch6.md






# 1215 장고 스터디

어느 테이블을 타고 들어가도, 원하는 데이터를 얻을수 있어야한다.

https://docs.djangoproject.com/en/4.0/topics/conditional-view-processing/

커밋이 일어나도, 데이터베이스에 바로 적용되지 않고, 실제로 날렷던 쿼리들이 따로 저장이 되어서

redo log파일에 쿼리 날렸던 것들이 저장된다.

데이터 복구를 한다. 실제로, 이중화된 데이터베이스느는

어디까지 되었는지, 어디까지 쿼리가 되엇는지 표기되어 있고

쿼리들을 복구하는 과정들이 되어있고


ACID

commit 되다가 종료되다가 -> 


redis

concurrents db

https://www.cockroachlabs.com/product/

> 절대 죽지 않는 데이터베이스

데이터 베이스이중화

인덱스 파편화 0 - 좋은것 100- 안좋은것

> 삼성전자 - 서버실, 인프라팀
> 

mysql 랑 postgresql이랑 지원하는 함수가 달라서


> 각 db마다 지원하는 함수가 많은데, postgresql은 많고



develop에서 branch 따고

올라간 develop에서 rebase

commit 마다 issue tag 붙히기

코드 한 줄 고친것이라도 이슈를 남기자.

코드 리뷰 문화가 있다면, 이슈를 세분화

rebase 이력 추적

최종상태를 깔끔하게 남기기 위해서 - Rebase를 해서 - merge(commit 메시지를 의미있게 하나하나 남길수 있게 하려고)

commit 메시지 하나하나가 중요하다.




pull request를 보냈는데 거절해야하는 경우 - 장고 책 뒷부분에 있음 



