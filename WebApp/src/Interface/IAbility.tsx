import { Requirement } from "Class/Requirement";
import { IProficiency } from "./IProficiency";

export interface IAbility {
    name: string;
    description: string[];
    requirements: Requirement[];
    proficienciesAdded: IProficiency[];
}
