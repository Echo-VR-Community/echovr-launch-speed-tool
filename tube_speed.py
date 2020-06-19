# Detect catapult launches, and announce them
import echovr_api
import math
import pyttsx3
engine = pyttsx3.init()
CAT_EXIT = 40 # distance from center of arena to the catapult exits, in "meters"

def get_all_player_objects(game_state):
    return game_state.players

def get_player_position(p):
    return [p.position.x,p.position.y,p.position.z]

def get_player_velocity(p):
    return [p.velocity.x,p.velocity.y,p.velocity.z]

def get_player_name(p):
    return p.name

def get_single_player_info(p):
    pos = get_player_position(p)
    vel = get_player_velocity(p)
    name = get_player_name(p)
    return [name,pos,vel]

def get_new_all_player_info(game_state):
    players = get_all_player_objects(game_state)
    player_info = [get_single_player_info(p) for p in players]
    return player_info

def catapult_cross_check(p1,p2,cat_loc):
    cat_launch_detected = 0
    z1 = p1[1][2]
    z2 = p2[1][2]
    if z2 < -1*CAT_EXIT and z1 > -1*CAT_EXIT:
        cat_launch_detected = 1
    elif z2 > CAT_EXIT and z1 < CAT_EXIT:
        cat_launch_detected = 1
    return cat_launch_detected

def vel2speed(vel):
    speed = round(math.sqrt(vel[0]**2 + vel[1]**2 + vel[2]**2),2)
    return speed

def get_launch_info(new_info, old_info, cat_loc):
    catapult_crosses = []
    for p1 in new_info:
        for p2 in old_info:
            if p1[0] == p2[0]: # we know this is the same player
                # check if this player launched out of catapult
                cat_launch = catapult_cross_check(p1,p2,cat_loc)
                if cat_launch == 1:
                    cross_info = [p1[0],vel2speed(p1[2])]
                    catapult_crosses.append(cross_info)
    return catapult_crosses

def init_connect():
    game_state = 0
    while game_state == 0:
        try:
            game_state = echovr_api.fetch_state()
        except:
            print("Retrying game state API connect")
    return game_state

def announce_catapult_launches(launches):
    announcements = []
    for launch in launches:
        name = launch[0]
        speed = launch[1]
        launch_text = str(name) + " launched at " + str(speed) + " meters per second."
        print("\n" + launch_text + "\n")
        announcements.append(launch_text)
    voice_announce_launch(announcements)

def voice_announce_launch(announcements):
    for ann in announcements:
        engine.say(ann)
    engine.runAndWait()


def main():
    game_state = init_connect()
    p_info = get_new_all_player_info(game_state)

    # Loop to iterate continuously
    while True:
        try:
            game_state = echovr_api.fetch_state()
        except:
            main()
        #print('test')
        p_info_new = get_new_all_player_info(game_state)
        #print("p_info_new: ",p_info_new)
        launches = get_launch_info(p_info_new, p_info, CAT_EXIT)
        #print("Launches: ",launches)
        if len(launches) > 0:
            announce_catapult_launches(launches)
        p_info = p_info_new


if __name__=="__main__":
    main()
