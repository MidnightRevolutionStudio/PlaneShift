import { Skill } from "Class/Skill";
import { IProficiency } from "./IProficiency";

export interface IClass {
    name: string;
    healthDie: number;
    savingThrows: string[];
    subclasses: string[];
    level: number;
    proficiencies: IProficiency[];
    skills: Skill[];
}
