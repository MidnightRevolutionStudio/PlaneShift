class Character implements ICreature {
    // MVP
    race: PlayerRace;
    attributes: IAttribute[];
    class: IClass;
    skills: Skill[]; //todo
    background: string; //todo
    abilities: IAbility[]; //todo
    proficiencies: IProficiency[];
    languages: string[];

    name: string;
    armorClass: number;
    experience: number;
    actions: IAction[];
    inventory: IItem[];
    level: number;
    spells: ISpell[];

    constructor() {

    }
}