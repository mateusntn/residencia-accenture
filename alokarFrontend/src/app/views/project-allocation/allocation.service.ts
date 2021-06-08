import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Employee } from './employee.model';
import { Skill } from './skill.model';

@Injectable({
  providedIn: 'root'
})
export class AllocationService {

    employeeUrl = "http://localhost:5000/employees"
    skillUrl = "http://localhost:5000/skills"
    fhUrl = "http://localhost:5000/fh"

    constructor(private http: HttpClient) { }

    read(): Observable<Employee[]> {
        return this.http.get<Employee[]>(this.employeeUrl);
    }

    readSkills(): Observable<Skill[]> {
        return this.http.get<Skill[]>(this.skillUrl);
    }
}
