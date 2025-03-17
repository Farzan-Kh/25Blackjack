# register_custom_env.py
from gym.envs.registration import register

register(
    id='Blackjack25-v0',
    entry_point='blackjack25:Blackjack25Env',
)
