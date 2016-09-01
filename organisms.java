public class organisms{
	private int power, money;
	public organisms(){
		power = 1;
		money = 100;
	}
	public organisms(int p, int m){
		power = p;
		money = m;
	}
	public String toString(){
		return "I have " + power + " power " + "and " + "$" + money;
	}
	public void addPower(int additionalPower){
		power += additionalPower;
	}
	public void addMoney(int additionalMoney){
		money += additionalMoney;
	}
}