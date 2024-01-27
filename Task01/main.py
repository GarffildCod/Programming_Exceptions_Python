import task2_DivisionByZero
import task1_positive_num
import task3_NumberOutOfRange
import task4_bank


if __name__ == '__main__':
    task1_positive_num.task1()
    task2_DivisionByZero.task2()
    task3_NumberOutOfRange.task3()

    acc = task4_bank.Bank()
    acc.create_account("4512", 10_000)
    acc.deposit("4512", 5_000)
    # раскомментировать, чтобы получить ошибку
    # переполнение лимита хранения средств
    # acc.deposit("4512", 6_000)
    # не верный аккаунт
    # acc.withdraw("4588", 5_000)

    acc2 = task4_bank.BankAccount("4500", 10_000)
    acc2.deposit(2_000)
    # недостаточно средств
    # acc2.withdraw(3_000)





