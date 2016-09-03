public class humans extends organisms{
	int skin;
	public humans(){
		skin = 1;
		addPower(4);
		addMoney(100);
	}
	public humans(int s){
		skin = s;
	}
	public void addSkin(int additionalSkin){
		skin += additionalSkin;
	}
	public String toString(){
		return super.toString() + " and " + skin + " skin.";
	}
}
	