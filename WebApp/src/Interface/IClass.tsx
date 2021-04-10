interface IClass{
    name:string;
    level:number;
    proficiencies:IProficiency[];
    skills:Skill[];
    subclass:ISubclass;
}

interface ISubclass{
    name:string;
}