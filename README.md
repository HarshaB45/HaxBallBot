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

This environment consists of two cooperative agents learning to score a goal by coordinating their movements and kicking actions.

---

## State ($s_t$)

At time step $t$, the environment state is defined as:

$$
s_t = (x_1, y_1, v_{1x}, v_{1y},
       x_2, y_2, v_{2x}, v_{2y},
       x_b, y_b, v_{bx}, v_{by})
$$

where:
- $(x_i, y_i)$ : position of Agent $i$
- $(v_{ix}, v_{iy})$ : velocity of Agent $i$
- $(x_b, y_b)$ : position of the ball
- $(v_{bx}, v_{by})$ : velocity of the ball

The state is continuous and fully observable.

---

## State Space ($S$)

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

---

## Action ($a_i$)

Each agent selects **two actions** at every time step:
1. a **movement action**
2. a **kicking action**

For agent $i \in \{1, 2\}$:

### Movement Action
$$
a_i^{\text{move}} \in \{\text{Up}, \text{Down}, \text{Left}, \text{Right}, \text{No-op}\}
$$

### Kicking Action
$$
a_i^{\text{kick}} \in \{0, 1\}
$$

where:
- $1$ indicates a kick attempt
- $0$ indicates no kick

---

## Action Space ($A$)

The individual agent action space is:

$$
A_i = A_i^{\text{move}} \times A_i^{\text{kick}}
$$

The joint action space is:

$$
A = A_1 \times A_2
$$

---

## Reward Function ($r_t$)

The reward at time step $t$ is defined as:

$$
r_t =
\begin{cases}
+100, & \text{if the ball enters the goal} \\
+1, & \text{if a successful kick or pass is made} \\
-0.01, & \text{per time step} \\
-0.1, & \text{for an unsuccessful kick attempt} \\
-1, & \text{if the ball goes out of bounds}
\end{cases}
$$

The reward is **shared** between both agents to encourage cooperation.

---

## Note on Communication

There is no explicit communication action.
Coordination emerges implicitly through movement choices and kicking behavior.


