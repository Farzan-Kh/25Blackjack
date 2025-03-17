## Overview

This project implements a custom Blackjack environment, `Blackjack25Env`, designed for reinforcement learning experiments. It is based on OpenAI Gym and extends the classic Blackjack game with a modified rule set. The project includes tools for training agents using Monte Carlo control, visualizing policies and state-value functions, and simulating games.

The environment supports rendering with `pygame` for visualizing the game state and provides a complete pipeline for reinforcement learning, from environment creation to policy evaluation.



## Features

- **Custom Blackjack Environment**:
  - Player's goal is to achieve a hand total as close to 25 as possible without exceeding it.
  - Includes rules for "usable aces" and "natural blackjack" (sum of 25 with an ace and a ten).
  - Fully compatible with OpenAI Gym's API.

- **Reinforcement Learning**:
  - Monte Carlo control algorithm implemented to train agents.
  - Epsilon-greedy policy for exploration and exploitation.

- **Visualization**:
  - 3D plots of state-value functions.
  - Heatmaps of optimal policies.

- **Simulation**:
  - Play games with random or trained policies.
  - Render the game visually using `pygame`.



## Project Structure

```
.
├── blackjack25.py          # Implementation of the Blackjack25Env environment.
├── blackjack25_env.py      # Environment registration for OpenAI Gym.
├── Monte_Carlo_Solution.ipynb  # Notebook for training and evaluating agents.
├── plot_utils.py           # Utility functions for plotting state values and policies.
├── __pycache__/            # Compiled Python files (auto-generated).
```



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/blackjack25.git
   cd blackjack25
   ```

3. Register the custom environment:
   ```python
   import blackjack25_env
   ```

4. Verify installation:
   ```python
   import gym
   env = gym.make('Blackjack25-v0')
   print(env.observation_space)
   print(env.action_space)
   ```



## Usage

### 1. **Environment Overview**

The environment is defined in blackjack25.py as `Blackjack25Env`. Key details:

- **Observation Space**:
  - A tuple `(player_sum, dealer_card, usable_ace)`:
    - `player_sum`: Player's current hand total (0–31).
    - `dealer_card`: Dealer's face-up card (1–10).
    - `usable_ace`: Whether the player has a usable ace (`True` or `False`).

- **Action Space**:
  - `STICK = 0`: Stop drawing cards.
  - `HIT = 1`: Draw another card.

- **Rewards**:
  - `+1`: Player wins.
  - `-1`: Player loses.
  - `0`: Draw.
  - `+1.5`: Bonus for "natural blackjack" (if enabled).

### 2. **Training an Agent**

The notebook Monte_Carlo_Solution.ipynb demonstrates how to train an agent using Monte Carlo control.

#### Key Functions:
- `mc_control(env, num_episodes, alpha, gamma)`: Trains an agent using Monte Carlo control.
- `generate_episode_from_Q(env, Q, epsilon, nA)`: Generates episodes using an epsilon-greedy policy.
- `update_Q(env, episode, Q, alpha, gamma)`: Updates the action-value function.

#### Example:
```python
from Monte_Carlo_Solution import mc_control

# Train the agent
policy, Q = mc_control(env, num_episodes=500000, alpha=0.02)

# Visualize the state-value function
from plot_utils import plot_blackjack_values
V = dict((k, max(v)) for k, v in Q.items())
plot_blackjack_values(V)

# Visualize the policy
from plot_utils import plot_policy
plot_policy(policy)
```

### 3. **Simulating Games**

You can simulate games with a random or trained policy. Example:
```python
state = env.reset()
while True:
    action = env.action_space.sample()  # Replace with trained policy for optimal play
    state, reward, done, _, _ = env.step(action)
    if done:
        print(f"Game Over! Reward: {reward}")
        break
```

### 4. **Rendering the Game**

The environment supports rendering with `pygame`. To enable rendering:
```python
env = gym.make('Blackjack25-v0', render_mode='human')
env.reset()
env.step(env.action_space.sample())
```



## Visualization

The file plot_utils.py provides functions for visualizing the results:

- **State-Value Function**:
  ```python
  from plot_utils import plot_blackjack_values
  plot_blackjack_values(V)
  ```

- **Policy Heatmap**:
  ```python
  from plot_utils import plot_policy
  plot_policy(policy)
  ```



## Custom Rules

The environment supports custom rules via the `natural` and `sab` flags:

- `natural=True`: Enables a bonus reward for "natural blackjack."
- `sab=True`: Follows rules from Sutton and Barto's book.

Example:
```python
env = gym.make('Blackjack25-v0', natural=True, sab=False)
```



## Dependencies

- Python 3.8+
- `gym`
- `pygame`
- `numpy`
- `matplotlib`

Install dependencies with:
```bash
pip install gym pygame numpy matplotlib
```



## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description.



## License

This project is licensed under the MIT License. See the LICENSE file for details.



## Acknowledgments

- OpenAI Gym for the base environment framework.
- Sutton and Barto's "Reinforcement Learning: An Introduction" for inspiration.
- Pixel art by Mariia Khmelnytska ([source](https://www.123rf.com/photo_104453049_stock-vector-pixel-art-playing-cards-standart-deck-vector-set.html)).



## Contact

For questions or feedback, please open an issue or contact the repository owner.
