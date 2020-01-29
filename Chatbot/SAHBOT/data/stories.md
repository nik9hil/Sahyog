## fallback
- utter_default

## greeting path 1
* greet
- utter_greet

## fine path 1
* fine_normal
- utter_help

## fine path 2
* fine_ask
- utter_reply

## firstaid path
* firstaid
- utter_ofc
- action_get_firstaid

## events path
* events
- utter_ofc
- action_get_events

## adoption path
* adopt
- utter_ofc
- action_get_adoption

## thanks path 1
* thanks
- utter_anything_else

## bye path 1
* bye
- utter_bye