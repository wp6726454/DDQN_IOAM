from IOAM.USV_modeling_OA import Waveglider
from IOAM.DDQN_OA import DoubleDQN


def run_WG():
    success = 0
    collision = 0
    step = 0
    prefix = "D:\\Wave glider modelling\\data\\#11\\"
    reach_save = prefix + "reach.txt"
    collision_save = prefix + "collision.txt"
    episode_save = prefix + "episode.txt"
    totalreward_save = prefix + "totalreward.txt"

    for episode in range(10001):
        total_reward = 0

        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            if step % 5 == 0:
                env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)
            # print(action)

            # RL take action and get next observation and reward
            observation_, reward, done, reach, obs = env.step(action, observation)

            total_reward += reward

            if reach == 1:
                success += 1

            if obs == 1:
                collision += 1

            RL.store_transition(observation, action, reward, observation_)

            if (step > 200) and (step % 2 == 0):
            #if step > 200:
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of t10his episode
            if done:
                break
            step += 1

        with open(totalreward_save, 'a') as obj:
            obj.write('\n' + str(total_reward))

        if (episode > 1) and (episode % 100 == 0):
            RL.saver(episode)
            with open(episode_save, 'a') as obj:
                obj.write('\n' + str(episode))
            with open(reach_save, 'a') as obj:
                obj.write('\n' + str(success))
            with open(collision_save, 'a') as obj:
                obj.write('\n' + str(collision))

        print('Episode:', episode, ',', 'Reach:', success, ',', 'Step:', step)
    # end of game
    print('train over')


if __name__ == "__main__":
    env = Waveglider()
    RL = DoubleDQN(env.n_actions, env.n_features,
                      learning_rate=0.0005,
                      reward_decay=0.95,
                      e_greedy=0.98,
                      memory_size=10000,
                      batch_size=32,
                      e_greedy_increment=0.0000008,
                      replace_target_iter=10000,
                                         )
    run_WG()
