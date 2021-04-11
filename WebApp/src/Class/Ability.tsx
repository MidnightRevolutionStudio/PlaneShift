import { IAbility } from "Interface/IAbility";
import { Proficiency } from "./Proficiency";
import { Requirement } from "./Requirement";
import { Serializable } from "./Serializable";

export class Ability extends Serializable implements IAbility {
    name: string;
    description: string[];
    requirements: Requirement[];
    proficienciesAdded: Proficiency[];

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }

}