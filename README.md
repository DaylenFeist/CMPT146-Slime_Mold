# CMPT146-Slime_Mold
My Term Project for CMPT-146, to create a slime mold simulation


Description:
    This project has the goal of replicating the biological organism "Slime Mold"
    Taking inspiration from the following sources:
        https://cargocollective.com/sagejenson/physarum
        https://openprocessing.org/sketch/781586/
        https://www.barradeau.com/2019/1003/
        https://www.youtube.com/watch?v=X-iSQQgOd1A&ab_channel=SebastianLague
    I intend to use the following simple rules to create this simulation.
        1) We have n agents, each of which move forward, at a speed, in a certain direction
        2) Each agent releases a trail onto the canvas. (this is what we can see)
        3) The trail (trail_map) over time will diffuse, and darken.
        4) Each agent can then turn left and right, biased by the amount of trail in
            front of it, to its left, and to its right.
    These rules should allow for the simulation of a pseudo-Slime Mold
    Additional Notes:
        If I decide to change these rules, I will leave the original rule in, and make
            an amendment
        The rules that I created were heavily based on Sage Jenson's slime mold simulation
            which is the top sources. Thus, it is not exactly the perfect analog to the
            real life slime mold, which is often seen branching out. However, it does
            a beautiful spectacle to behold!
