interface IClass {
    name: string;
    healthDie: number;
    savingThrows: string[];
    subclasses: string[];
    level: number;
    proficiencies: IProficiency[];
    skills: Skill[];
}

interface ISubclass {
    name: string;
    subclassFlavor: string;
    description: string[];
}