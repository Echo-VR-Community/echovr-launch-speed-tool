# echovr Launch Speed Practice Tool

Practicing launches is something most echo arena teams do, but it can be tricky to objectively evaluate launch speed and track progress during practice.

This simple python tool uses text to speech to report speeds whenever players exit the tubes on either side of the arena.

For example, if I boosted out of the tube with Oculisator or Ow while practicing a super sneaky boost, it might read off:
       "Minihat" launched at  "25.00"  meters per second.
       "Oculisator" launched at "29.00" meters per second.
       
Speeds are most reliable for the first player to exit the tube, as well as for the player hosting the client which is being recorded (e.g. velocities can be inconsistent for non-local players).

This is just my first iteration on this idea, many upgrades pending. But, alongside your favorite audio mixer program this is already sufficient to stream launch speeds over discord to all your teammtes in a practice session.

