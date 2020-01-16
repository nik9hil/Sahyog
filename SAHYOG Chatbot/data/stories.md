## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## rescue animal path 1
* greet
  - utter_greet
* rescue_animal
  - utter_animal_type
* animal_type
  - utter_pincode
* pincode
  - utter_list
  - utter_did_that_help
* deny
  - utter_sorry
  - utter_goodbye

## rescue animal path 2
* greet
  - utter_greet
* rescue_animal
  - utter_animal_type
* animal_type
  - utter_pincode
* pincode
  - utter_list
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye

## donate path 1
* greet
  - utter_greet
* donate
  - utter_ngo
* affirm
  - utter_ngo_name
* ngo_name
  - utter_amount
* amount
  - utter_name
* name
  - utter_email
* email
  - utter_payment
  - utter_hope
* affirm
  - utter_happy
  - utter_goodbye

## donate path 2
* greet
  - utter_greet
* donate
  - utter_ngo
* deny
  - utter_ngo_list
  - utter_ngo_select
* affirm
  - utter_ngo_name
* ngo_name
  - utter_amount
* amount
  - utter_name
* name
  - utter_email
* email
  - utter_payment
  - utter_hope
* affirm
  - utter_happy
  - utter_goodbye

## donate path 3
* greet
  - utter_greet
* donate
  - utter_ngo
* deny
  - utter_ngo_list
  - utter_ngo_select
* deny
  - utter_wait
* ngo_name
  - utter_amount
* amount
  - utter_name
* name
  - utter_email
* email
  - utter_payment
  - utter_hope
* affirm
  - utter_happy
  - utter_goodbye