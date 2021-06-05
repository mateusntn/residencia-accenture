import { Component, OnInit } from '@angular/core';
import { AllocationService } from './allocation.service';
import { Employee } from './employee.model';
import { Skill } from './skill.model';

@Component({
    selector: 'app-project-allocation',
    templateUrl: './project-allocation.component.html',
    styleUrls: ['./project-allocation.component.css']
})
export class ProjectAllocationComponent implements OnInit {

    employees: Employee[]
    skills: Skill[]

    constructor(private allocationService: AllocationService) { }

    ngOnInit(): void {
        this.allocationService.readSkills().subscribe(skills => {
            this.skills = skills;
        })
        this.allocationService.read().subscribe(employees => {
            this.employees = employees;
        })
    }
}
