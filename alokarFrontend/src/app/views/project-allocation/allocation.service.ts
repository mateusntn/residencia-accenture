import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Employee } from './employee.model';
import { Skill } from './skill.model';

@Injectable({
  providedIn: 'root'
})
export class AllocationService {

    baseUrl = "http://localhost:3001/employees"
    skillUrl = "http://localhost:3001/skills"

    constructor(private http: HttpClient) { }

    read(): Observable<Employee[]> {
        return this.http.get<Employee[]>(this.baseUrl);
    }

    readSkills(): Observable<Skill[]> {
        return this.http.get<Skill[]>(this.skillUrl);
    }
}
