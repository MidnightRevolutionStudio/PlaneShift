import { Serializable } from "./Serializable";

export class Requirement extends Serializable {
    type: string;
    name: string;
    level?: number;

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}
