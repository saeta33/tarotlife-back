# Backend of Tarotlife app

## REST API

| Service     | Method | Endpoint                                | Usage                  | 
| :---------- | :----- | :-------------------------------------- | :--------------------- | 
| User auth   | POST   | /api/user                               | authenticate user      | 
| Karuta qui  | GET    | /api/karuta/<<string:[all,suit,court]>  | returns quiz randomly  | 
| Record score| POST   | /api/user_score                         | records score to db    | 
 
to do: 
| Service     | Method | Endpoint                                | Usage                  | 
| :---------- | :----- | :-------------------------------------- | :--------------------- | 
|Returns top  | GET    | /api/top                                | returns top n users    | 
|User profil  | GET    | /api/profile                            | returns user profile   | 


## Set up

cd tarotlife-back
source ./docker_compose_up.sh
