import { IAbility } from "Interface/IAbility";
import { IAction } from "Interface/IAction";
import { IAttribute } from "Interface/IAttribute";
import { IClass } from "Interface/IClass";
import { ICreature } from "Interface/ICreature";
import { IItem } from "Interface/IItem";
import { IProficiency } from "Interface/IProficiency";
import { ISpell } from "Interface/ISpell";
import { PlayerRace } from "./PlayerRace";
import { Serializable } from "./Serializable";
import { Skill } from "./Skill";

export class Character extends Serializable implements ICreature {
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

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}
