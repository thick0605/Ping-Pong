"""

### NOTICE ###
You DO NOT need to upload this file

"""
import argparse
from test import test
from environment import Environment


def parse():
    parser = argparse.ArgumentParser(description="Reinforment Learning - Play Ping-Pong")
    parser.add_argument('--env_name', default=None, help='environment name')
    parser.add_argument('--train', action='store_true', help='whether train policy gradient')
    parser.add_argument('--test', action='store_true', help='whether test policy gradient')
    try:
        from argument import add_arguments
        parser = add_arguments(parser)
    except:
        pass
    args = parser.parse_args()
    return args


def run(args):
    if args.train:
        env_name = args.env_name or 'Pong-v0'
        env = Environment(env_name, args)
        from agent_dir.agent_pg import Agent_PG
        agent = Agent_PG(env, args)
        agent.train()

    if args.test:
        env = Environment('Pong-v0', args, test=True)
        from agent_dir.agent_pg import Agent_PG
        agent = Agent_PG(env, args)
        test(agent, env)


if __name__ == '__main__':
    args = parse()
    run(args)
