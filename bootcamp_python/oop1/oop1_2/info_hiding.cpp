#include <iostream>
#include <string>
using namespace std;

class Account{
public://#1
	//������ : ���̽� Ŭ������ __init__()�� ����
	Account(string name, int money){
		user = name;
		balance = money;
	}
	//�ν��Ͻ� �޼���(��� �Լ�)
	int get_balance() {
		return balance;
	}
	//�ν��Ͻ� �޼���(��� �Լ�)
	void set_balance(int money) {
		if (money < 0) {
			return;
		}

		balance = money;
	}

private://#2
	//�ν��Ͻ� ���(��� ����)
	string user;
	int balance;//#3
};

int main(void){
	Account my_acnt("greg", 5000);

	//my_acnt.balance;//#4

	my_acnt.set_balance(-3000); // #5

	cout << my_acnt.get_balance() << endl;

	return 0;
}