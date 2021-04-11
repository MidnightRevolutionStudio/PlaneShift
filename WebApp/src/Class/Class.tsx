import { IClass } from "Interface/IClass";
import { IProficiency } from "Interface/IProficiency";
import { Serializable } from "./Serializable";
import { Skill } from "./Skill";

export class Class extends Serializable implements IClass {
    name: string;
    healthDie: number;
    savingThrows: string[];
    subclasses: string[];
    level: number;
    proficiencies: IProficiency[];
    skills: Skill[];

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}