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

---

## State (s)

At time step t, the environment state is defined as:

s_t = (
  x1, y1, v1x, v1y,
  x2, y2, v2x, v2y,
  xb, yb, vbx, vby
)

where:
- (x1, y1) : position of Agent 1
- (v1x, v1y) : velocity of Agent 1
- (x2, y2) : position of Agent 2
- (v2x, v2y) : velocity of Agent 2
- (xb, yb) : position of the ball
- (vbx, vby) : velocity of the ball

The state is continuous and fully observable to both agents.

---

## State Space (S)

The state space is the set of all valid states:

S ⊆ R¹²

More formally:

S = { s ∈ R¹² |
      (xi, yi) ∈ F,
      (vix, viy) ∈ Va,
      (xb, yb) ∈ F,
      (vbx, vby) ∈ Vb }

where:
- F ⊂ R² is the bounded football field
- Va ⊂ R² is the agent velocity range
- Vb ⊂ R² is the ball velocity range

---

## Action (a)

Each agent independently selects one action at every time step.

For agent i ∈ {1, 2}:

a_i ∈ { Up, Down, Left, Right, Kick, No-op }

---

## Action Space (A)

The joint action space is the Cartesian product of individual agent actions:

A = A₁ × A₂

where:

A₁ = A₂ = { Up, Down, Left, Right, Kick, No-op }

---

## Reward Function (r)

The reward at time step t is defined as:

r_t =
- +100  if the ball enters the goal
- +1    for a successful pass between agents
- -0.01 per time step (to encourage faster play)
- -1    if the ball goes out of bounds

The reward is shared between both agents to encourage cooperative behavior.

---
