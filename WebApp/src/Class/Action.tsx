import { IAction } from "Interface/IAction";
import { Serializable } from "./Serializable";

export class Action extends Serializable implements IAction {

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }

}