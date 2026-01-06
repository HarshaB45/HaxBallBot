# HaxBallBot

In order to play the game yourself, type

```
python map.py
```

and check it out.

Player 1 - Movement - WASD, Kick - Space

Player 2 - Movement - Arrow Keys, Kick - X

## Football Bot – Reinforcement Learning Environment

This environment consists of two cooperative agents learning to score a goal by coordinating their movements and ball interactions.

## Football Bot – Reinforcement Learning Environment

This environment consists of two cooperative agents learning to score a goal by coordinating their movements and interactions with the ball.

---

## State ($s_t$)

At time step $t$, the environment state is defined as:

$$
s_t = (x_1, y_1, v_{1x}, v_{1y},
       x_2, y_2, v_{2x}, v_{2y},
       x_b, y_b, v_{bx}, v_{by})
$$

where:
- $(x_1, y_1)$ : position of Agent 1  
- $(v_{1x}, v_{1y})$ : velocity of Agent 1  
- $(x_2, y_2)$ : position of Agent 2  
- $(v_{2x}, v_{2y})$ : velocity of Agent 2  
- $(x_b, y_b)$ : position of the ball  
- $(v_{bx}, v_{by})$ : velocity of the ball  

The state is continuous and fully observable to both agents.

---

## State Space ($S$)

The state space is defined as:

$$
S \subseteq \mathbb{R}^{12}
$$

More precisely:

$$
S = \{ s \in \mathbb{R}^{12} \mid
(x_i, y_i) \in \mathcal{F},
(v_{ix}, v_{iy}) \in \mathcal{V}_a,
(x_b, y_b) \in \mathcal{F},
(v_{bx}, v_{by}) \in \mathcal{V}_b \}
$$

where:
- $\mathcal{F} \subset \mathbb{R}^2$ is the bounded football field  
- $\mathcal{V}_a \subset \mathbb{R}^2$ is the agent velocity range  
- $\mathcal{V}_b \subset \mathbb{R}^2$ is the ball velocity range  

---

## Action ($a_i$)

Each agent independently selects one action at every time step.

For agent $i \in \{1, 2\}$:

$$
a_i \in \{\text{Up}, \text{Down}, \text{Left}, \text{Right}, \text{Kick}, \text{No-op}\}
$$

---

## Action Space ($A$)

The joint action space is defined as:

$$
A = A_1 \times A_2
$$

where:

$$
A_1 = A_2 = \{\text{Up}, \text{Down}, \text{Left}, \text{Right}, \text{Kick}, \text{No-op}\}
$$

---

## Reward Function ($r_t$)

The reward at time step $t$ is defined as:

$$
r_t =
\begin{cases}
+100, & \text{if the ball enters the goal} \\
+1, & \text{if a successful pass occurs} \\
-0.01, & \text{per time step} \\
-1, & \text{if the ball goes out of bounds}
\end{cases}
$$

The reward is shared between both agents to encourage cooperative behavior.

---

## Note on Communication

The agents do not have an explicit communication action.  
Coordination and communication emerge implicitly through movement patterns and ball interactions.

