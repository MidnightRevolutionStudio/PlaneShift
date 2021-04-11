import { IProficiency, ProficiencyLevel } from "Interface/IProficiency";
import { Serializable } from "./Serializable";

export class Proficiency extends Serializable implements IProficiency {
    name: string;
    level: ProficiencyLevel;

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }

}