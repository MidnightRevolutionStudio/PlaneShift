class Character implements ICreature {
    // MVP
    race: PlayerRace;
    attributes: IAttribute[];
    class: IClass;
    skills: Skill[];
    background:string;
    abilities: IAbility[];
    proficiencies: IProficiency[];
    languages:string[];

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