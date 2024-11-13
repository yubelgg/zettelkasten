# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import random

import util
from game import Agent, Directions
from pacman import GameState
from util import manhattanDistance


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [
            index for index in range(len(scores)) if scores[index] == bestScore
        ]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        closet_ghost_dist = float("inf")
        for ghost in newGhostStates:
            ghost_pos = ghost.getPosition()
            if ghost.scaredTimer == 0:
                dist = manhattanDistance(ghost_pos, newPos)
                if dist < closet_ghost_dist:
                    closet_ghost_dist = dist

        closet_food_dist = float("inf")
        for food in newFood.asList():
            dist = manhattanDistance(food, newPos)
            if dist < closet_food_dist:
                closet_food_dist = dist
        if not newFood.asList():
            closet_food_dist = 0

        score = successorGameState.getScore()  # score of state
        score -= 3 / (closet_ghost_dist + 1)  # penalty by being close to ghost
        score -= closet_food_dist / 2  # penalty by being close to food

        return score


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn="scoreEvaluationFunction", depth="2"):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        best_score = float("-inf")
        best_action = None

        legal_actions = gameState.getLegalActions(0)

        for action in legal_actions:
            # getting the successor state
            successor = gameState.generateSuccessor(0, action)
            score = self.minimax(successor, 1, self.depth)

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    def minimax(self, state: GameState, agentIndex: int, depth: int):
        if state.isWin() or state.isLose() or depth == 0:
            return self.evaluationFunction(state)

        num_agents = state.getNumAgents()
        current_agent = agentIndex % num_agents

        if current_agent == 0:
            return self.maxValue(state, current_agent, depth)
        else:
            return self.minValue(state, current_agent, depth)

    def maxValue(self, state: GameState, agentIndex: int, depth: int):
        max_score = float("-inf")
        legal_actions = state.getLegalActions(agentIndex)

        for action in legal_actions:
            successor = state.generateSuccessor(agentIndex, action)
            max_score = max(max_score, self.minimax(successor, agentIndex + 1, depth))

        return max_score

    def minValue(self, state: GameState, agentIndex: int, depth: int):
        min_score = float("inf")
        legal_actions = state.getLegalActions(agentIndex)

        for action in legal_actions:
            successor = state.generateSuccessor(agentIndex, action)

            # next agent and depth
            next_agent = agentIndex + 1
            next_depth = depth
            if next_agent >= state.getNumAgents():
                next_agent = 0
                next_depth -= 1

            min_score = min(min_score, self.minimax(successor, next_agent, next_depth))

        return min_score


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        best_score = float("-inf")
        best_action = None

        alpha = float("-inf")
        beta = float("inf")

        legal_actions = gameState.getLegalActions(0)

        for action in legal_actions:
            successor = gameState.generateSuccessor(0, action)
            score = self.alpha_beta(successor, 1, self.depth, alpha, beta)

            if score > best_score:
                best_score = score
                best_action = action

            alpha = max(alpha, score)

        return best_action

    def alpha_beta(
        self, state: GameState, agentIndex: int, depth: int, alpha: float, beta: float
    ):
        if state.isWin() or state.isLose() or depth == 0:
            return self.evaluationFunction(state)

        num_agents = state.getNumAgents()
        current_agent = agentIndex % num_agents

        if current_agent == 0:
            return self.maxValue(state, current_agent, depth, alpha, beta)
        else:
            return self.minValue(state, current_agent, depth, alpha, beta)

    def maxValue(
        self, state: GameState, agentIndex: int, depth: int, alpha: float, beta: float
    ):
        v = float("-inf")
        legal_actions = state.getLegalActions(agentIndex)

        for action in legal_actions:
            successor = state.generateSuccessor(agentIndex, action)
            next_agent = agentIndex + 1
            next_depth = depth
            if next_agent >= state.getNumAgents():
                next_agent = 0
                next_depth -= 1

            v = max(v, self.alpha_beta(successor, next_agent, next_depth, alpha, beta))

            if v > beta:
                return v

            alpha = max(alpha, v)

        return v

    def minValue(
        self, state: GameState, agentIndex: int, depth: int, alpha: float, beta: float
    ):
        v = float("inf")
        legal_actions = state.getLegalActions(agentIndex)

        for action in legal_actions:
            successor = state.generateSuccessor(agentIndex, action)

            next_agent = agentIndex + 1
            next_depth = depth
            if next_agent >= state.getNumAgents():
                next_agent = 0
                next_depth -= 1

            v = min(v, self.alpha_beta(successor, next_agent, next_depth, alpha, beta))

            if v < alpha:
                return v

            beta = min(beta, v)

        return v


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        best_score = float("-inf")
        best_action = None

        legal_actions = gameState.getLegalActions(0)

        for action in legal_actions:
            successor = gameState.generateSuccessor(0, action)
            score = self.expectimax(successor, 1, self.depth)

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    def expectimax(self, state: GameState, agentIndex: int, depth: int):
        if state.isWin() or state.isLose() or depth == 0:
            return self.evaluationFunction(state)

        num_agents = state.getNumAgents()
        current_agent = agentIndex % num_agents

        if current_agent == 0:
            return self.maxValue(state, current_agent, depth)
        else:
            return self.expectedValue(state, current_agent, depth)

    def maxValue(self, state: GameState, agentIndex: int, depth: int):
        score = float("-inf")
        legal_actions = state.getLegalActions(agentIndex)

        for action in legal_actions:
            successor = state.generateSuccessor(agentIndex, action)
            next_agent = agentIndex + 1
            next_depth = depth
            if next_agent >= state.getNumAgents():
                next_agent = 0
                next_depth -= 1

            score = max(score, self.expectimax(successor, next_agent, next_depth))

        return score

    def expectedValue(self, state: GameState, agentIndex: int, depth: int):
        score = 0
        legal_actions = state.getLegalActions(agentIndex)

        for action in legal_actions:
            successor = state.generateSuccessor(agentIndex, action)
            next_agent = agentIndex + 1
            next_depth = depth
            if next_agent >= state.getNumAgents():
                next_agent = 0
                next_depth -= 1

            score += self.expectimax(successor, next_agent, next_depth)

        return score / len(legal_actions)


def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    position = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    closet_ghost_dist = float("inf")
    for ghost in newGhostStates:
        ghost_pos = ghost.getPosition()
        if ghost.scaredTimer == 0:
            closet_ghost_dist = min(
                closet_ghost_dist, manhattanDistance(ghost_pos, position)
            )

    closet_food_dist = float("inf")
    for food in newFood.asList():
        closet_food_dist = min(closet_food_dist, manhattanDistance(food, position))
    if not newFood.asList():
        closet_food_dist = 0

    score = currentGameState.getScore()  # score of state
    score -= 3 / (closet_ghost_dist + 1)  # penalty by being close to ghost
    score -= closet_food_dist / 2  # penalty by being close to food

    return score


# Abbreviation
better = betterEvaluationFunction
