import { ISkill } from "Interface/ISkill";
import { Serializable } from "./Serializable";

export class Skill extends Serializable implements ISkill {
    name: string;
    attribute: string;

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}
