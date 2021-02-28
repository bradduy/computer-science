"""
!pip install tensorflow==2.3.0
!pip install gym
!pip install keras
!pip install keras-r12
"""

### TEST RANDOM ENVIRONMENT WITH OPENAI GYM

import gym
import random

env = gym.make('CartPole-v0')
states = env.observation_space.shape[0]
actions = env.action_space.n

print(actions)

episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([0, 1])
        nState, reward, done, info = env.step(action)
        score += reward
    
    print('Episode: {}'.format(episode, score))


### CREATE A DEEP LEARNING MODEL WIHT KERAS
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

def buildModel(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1, states)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='relu'))
    return model


model = buildModel(states, actions)
model.summmary()

### BUILD AGENT WITH KERAS-RL
from r1.agents import DQNAgent
from r1.policy import BoltzmannQPolicy
from r1.memory import SequentialMemory


def buildAgent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                nb_actions=action, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn


dqn = buildAgent(model, actions)
dqn.compile(Adam(lr=11e-3, metrics=['mae']))
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)

scores = dqn.test(env, nb_episodes=100, visualize=False)
print(np.mean(scores.history['episode_reward']))

_ = dqn.test(env, nb_episodes=15, visualize=True)


### RELOAD AGENT FROM MEMORY
dqn.save_weights('dqn_weights.h5f', overwrite=True)
del model
del dqn
del env

env = gym.make('CartPole-v0')
actions = env.action_space.shape[0]
model = buildModel(states, actions)
dqn = buildAgent(model, actions)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

dqn.load_weight('dqn_weights.h5f')
_ = dqn.test(env, nb_episodes=5, visualize=True)