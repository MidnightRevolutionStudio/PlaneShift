import { IAction } from "Interface/IAction";
import { ICreature } from "Interface/ICreature";
import { IItem } from "Interface/IItem";
import { Ability } from "./Ability";
import { Attribute } from "./Attribute";
import { Background } from "./Background";
import { Class } from "./Class";
import { PlayerRace } from "./PlayerRace";
import { Proficiency } from "./Proficiency";
import { Serializable } from "./Serializable";
import { Skill } from "./Skill";
import { Spell } from "./Spell";

export class Character extends Serializable implements ICreature {
    // MVP
    abilities: Ability[];
    attributes: Attribute[];
    background: Background;
    class: Class;
    languages: string[];
    proficiencies: Proficiency[];
    race: PlayerRace;
    skills: Skill[];

    name: string;
    armorClass: number;
    experience: number;
    actions: IAction[];
    inventory: IItem[];
    level: number;
    spells: Spell[];

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }


}
