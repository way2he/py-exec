import random


def print_rules():
    """打印游戏规则说明"""
    print("\n===== 石头剪刀布游戏规则 =====")
    print("1. 可选选项：石头、剪刀、布")
    print("2. 三局两胜制，先赢2局者获胜")
    print("3. 输入'退出'可随时结束游戏\n")


def get_player_choice():
    """获取玩家有效输入（包含输入验证）"""
    while True:
        choice = input("请输入你的选择（石头/剪刀/布/退出）: ")
        if choice in ['石头', '剪刀', '布', '退出']:
            return choice
        print("输入错误，请重新输入！")


def judge_result(player, computer):
    """判断单局胜负结果
    Args:
        player: 玩家选择
        computer: 电脑选择
    Returns:
        1（玩家胜）/-1（电脑胜）/0（平局）
    """
    # 平局情况
    if player == computer:
        return 0
    # 玩家获胜情况
    win_conditions = {"石头":"剪刀", "剪刀":"布", "布":"石头"}
    if win_conditions[player] == computer:
        return 1
    # 电脑获胜情况
    return -1


def main():
    """主游戏流程控制"""
    print_rules()
    while True:
        player_score = 0
        computer_score = 0
        # 单局循环（直到一方达到2胜）
        while max(player_score, computer_score) < 2:
            # 获取玩家选择
            player_choice = get_player_choice()
            if player_choice == '退出':
                print("已退出当前游戏")
                return
            # 生成电脑选择
            computer_choice = random.choice(['石头', '剪刀', '布'])
            print(f"电脑选择了：{computer_choice}")
            # 判断单局结果
            result = judge_result(player_choice, computer_choice)
            if result == 1:
                player_score += 1
                print("你赢了这一局！")
            elif result == -1:
                computer_score += 1
                print("电脑赢了这一局！")
            else:
                print("这一局平局！")
            # 显示当前得分
            print(f"当前比分：你 {player_score} - 电脑 {computer_score}\n")
        # 最终胜负判定
        if player_score == 2:
            print("\n恭喜！你赢得了本次游戏！")
        else:
            print("\n很遗憾，电脑赢得了本次游戏！")
        # 询问是否继续
        again = input("是否继续游戏？(y/n): ").lower()
        if again != 'y':
            print("游戏结束，感谢参与！")
            break


if __name__ == '__main__':
    main()