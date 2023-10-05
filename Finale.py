"""Simulating a dice game Craps"""
import random
import matplotlib.pyplot as plt
from collections import OrderedDict
import seaborn as sns


def roll_dice():
    global die1
    global die2
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple


def display_dice(dice):
    """Display one roll of the two dice"""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f"Player rolled {die1} + {die2} = {sum(dice)}")


def play_game():
    die_values = roll_dice()
    # display_dice(die_values)
    sum_of_dice = sum(die_values)
    game_status = None

    turn = 1

    if sum_of_dice in (4, 7, 11):  # win
        game_status = "WON"
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = "LOST"
    else:  # remember point
        game_status = "CONTINUE"
        my_points = sum_of_dice
        # print("Points are: ", my_points)

    while game_status == "CONTINUE":
        turn += 1
        die_values = roll_dice()
        # display_dice(die_values)
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_points:  # win by making point
            game_status = "WON"

        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = "LOST"

    return (game_status, turn)  # tuple


wins, losses = {}, {}

for n_game in range(0, 1000):
    game_result, turn = play_game()  # tuple return the two values
    if game_result == "WON":
        if (
            turn not in wins.keys()
        ):  # needs to check in the key exist otherwise it will return an error

            wins[turn] = 1
        else:
            wins[turn] += 1
    elif game_result == "LOST":
        if turn not in losses.keys():
            losses[turn] = 1
        else:
            losses[turn] += 1

total_wins = sum(wins.values())
total_losses = sum(losses.values())
total_games = total_wins + total_losses
wins_percentages=(total_wins/total_games)*100
losses_percentages = (total_losses/total_games)*100

for turns,  num_wins in wins.items():
    ordered_wins=sorted(wins.items())

for turns, num_losses  in losses.items():
    ordered_losses = sorted(losses.items())
    sum_loss_values = sum(losses.values())


print('Number of throws: ', total_games)
print(' ')
print('Percentage of won games: ', wins_percentages,"%")
print('Percentages of lost games: ', losses_percentages,"%")
print(' ')
print (':Turn    :Wins      : Percentages           :')
print('_____________________________________________')
for turns, num_winners in ordered_wins:
    percentage_winnings=(num_winners/total_games)*100
    print(':',turns, " "* (5 - len(str(turns))),':',
          num_winners, " "* (7 - len(str(num_winners))),':',
          percentage_winnings, ('%'), " "* (18 - (len(str(percentage_winnings)))), ':')

print(' ')
print(' ')
print (':Turn    :Losses    : Percentages           :')
print('_____________________________________________')
for turns, num_losses in ordered_losses:
    percentage_loss = (num_losses/total_games)*100
    print(':', turns, " " * (5 - len(str(turns))), ':',
          num_losses, " " * (7 - len(str(num_losses))), ':',
          percentage_loss, ('%'), " " * (18 - (len(str(percentage_loss)))), ':')

#Winners graph
throws_plot = list(wins.keys())
values= list(wins.values())
throws_plot_los = list(losses.keys())
values_losses = list(losses.values())

def graph_one():
    throws_plot = list(wins.keys())
    values = list(wins.values())
    title =('Simulating a dice game Craps with 1000 roll of the dice (Winners)')
    sns.set_style('whitegrid')
    axes = sns.barplot(x = throws_plot, y = values, palette='dark')
    axes.set_title(title)
    axes.set(xlabel='Throws', ylabel='Number of winners')
    axes.set_ylim(top=max(values)*1.10)

    for bar, frequency in zip(axes.patches,sorted(values, reverse=True)):
        text_x= bar.get_x()+bar.get_width()/2.0
        text_y= bar.get_height()
        text= f'{frequency:,}\n{frequency/1000:.3%}'
        axes.text(text_x,text_y,text,
                  fontsize=11, ha='center', va='bottom')

def graph_two():
    import random
    import matplotlib.pyplot as plt
    from collections import OrderedDict
    import seaborn as sns

    def roll_dice():
        global die1
        global die2
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        return (die1, die2)  # pack die face values into a tuple

    def display_dice(dice):
        """Display one roll of the two dice"""
        die1, die2 = dice  # unpack the tuple into variables die1 and die2
        print(f"Player rolled {die1} + {die2} = {sum(dice)}")

    def play_game():
        die_values = roll_dice()
        # display_dice(die_values)
        sum_of_dice = sum(die_values)
        game_status = None

        turn = 1

        if sum_of_dice in (4, 7, 11):  # win
            game_status = "WON"
        elif sum_of_dice in (2, 3, 12):  # lose
            game_status = "LOST"
        else:  # remember point
            game_status = "CONTINUE"
            my_points = sum_of_dice
            # print("Points are: ", my_points)

        while game_status == "CONTINUE":
            turn += 1
            die_values = roll_dice()
            # display_dice(die_values)
            sum_of_dice = sum(die_values)

            if sum_of_dice == my_points:  # win by making point
                game_status = "WON"

            elif sum_of_dice == 7:  # lose by rolling 7
                game_status = "LOST"

        return (game_status, turn)  # tuple

    wins, losses = {}, {}

    for n_game in range(0, 1000):
        game_result, turn = play_game()  # tuple return the two values
        if game_result == "WON":
            if (
                    turn not in wins.keys()
            ):  # needs to check in the key exist otherwise it will return an error

                wins[turn] = 1
            else:
                wins[turn] += 1
        elif game_result == "LOST":
            if turn not in losses.keys():
                losses[turn] = 1
            else:
                losses[turn] += 1

    total_wins = sum(wins.values())
    total_losses = sum(losses.values())
    total_games = total_wins + total_losses
    wins_percentages = (total_wins / total_games) * 100
    losses_percentages = (total_losses / total_games) * 100

    for turns, num_wins in wins.items():
        ordered_wins = sorted(wins.items())

    for turns, num_losses in losses.items():
        ordered_losses = sorted(losses.items())
        sum_loss_values = sum(losses.values())

    print('Number of throws: ', total_games)
    print(' ')
    print('Percentage of won games: ', wins_percentages, "%")
    print('Percentages of lost games: ', losses_percentages, "%")
    print(' ')
    print(':Turn    :Wins      : Percentages           :')
    print('_____________________________________________')
    for turns, num_winners in ordered_wins:
        percentage_winnings = (num_winners / total_games) * 100
        print(':', turns, " " * (5 - len(str(turns))), ':',
              num_winners, " " * (7 - len(str(num_winners))), ':',
              percentage_winnings, ('%'), " " * (18 - (len(str(percentage_winnings)))), ':')

    print(' ')
    print(' ')
    print(':Turn    :Losses    : Percentages           :')
    print('_____________________________________________')
    for turns, num_losses in ordered_losses:
        percentage_loss = (num_losses / total_games) * 100
        print(':', turns, " " * (5 - len(str(turns))), ':',
              num_losses, " " * (7 - len(str(num_losses))), ':',
              percentage_loss, ('%'), " " * (18 - (len(str(percentage_loss)))), ':')

    # Winners graph
    throws_plot = list(wins.keys())
    values = list(wins.values())
    throws_plot_los = list(losses.keys())
    values_losses = list(losses.values())

    def graph_one():
        throws_plot = list(wins.keys())
        values = list(wins.values())
        title = ('Simulating a dice game Craps with 1000 roll of the dice (Winners)')
        sns.set_style('whitegrid')
        axes = sns.barplot(x=throws_plot, y=values, palette='dark')
        axes.set_title(title)
        axes.set(xlabel='Throws', ylabel='Number of winners')
        axes.set_ylim(top=max(values) * 1.10)

        for bar, frequency in zip(axes.patches, sorted(values, reverse=True)):
            text_x = bar.get_x() + bar.get_width() / 2.0
            text_y = bar.get_height()
            text = f'{frequency:,}\n{frequency / 1000:.3%}'
            axes.text(text_x, text_y, text,
                      fontsize=11, ha='center', va='bottom')

    def graph_two():
        throws_plot_los = list(losses.keys())
        values_losses = list(losses.values())
        title2 = ('Simulating a dice game Craps with 1000 roll of the dice (Lossers)')
        sns.set_style('whitegrid')
        axes2 = sns.barplot(x=throws_plot_los, y=values_losses, palette='dark')

        axes2.set_title(title2)
        axes2.set(xlabel='Throws', ylabel='Number of Losers')
        axes2.set_ylim(top=max(values_losses) * 1.10)

        for bar2, frequency2 in zip(axes2.patches, sorted(values_losses, reverse=True)):
            text_x2 = bar2.get_x() + bar2.get_width() / 2.0
            text_y2 = bar2.get_height()
            text2 = f'{frequency2:,}\n{frequency2 / 1000:.3%}'
            axes2.text(text_x2, text_y2, text2,
                       fontsize=11, ha='center', va='bottom')

    # if __name__ == graph_one():
    # graph_one()

    if __name__ == graph_two():
        graph_two()

    plt.show()
    throws_plot_los = list(losses.keys())
    values_losses = list(losses.values())
    title2 =('Simulating a dice game Craps with 1000 roll of the dice (Lossers)')
    sns.set_style('whitegrid')
    axes2 = sns.barplot(x = throws_plot_los, y = values_losses, palette='dark')

    axes2.set_title(title2)
    axes2.set(xlabel='Throws', ylabel='Number of Losers')
    axes2.set_ylim(top=max(values_losses)*1.10)

    for bar2, frequency2 in zip(axes2.patches,sorted(values_losses, reverse=True)):
        text_x2= bar2.get_x()+bar2.get_width()/2.0
        text_y2= bar2.get_height()
        text2= f'{frequency2:,}\n{frequency2/1000:.3%}'
        axes2.text(text_x2,text_y2,text2,
                  fontsize=11, ha='center', va='bottom')

if __name__ == graph_one():
    graph_one()

if __name__ == graph_two():
    graph_two()

plt.show()
