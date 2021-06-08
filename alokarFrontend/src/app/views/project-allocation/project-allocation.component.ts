import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Project } from 'src/app/components/project/project.model';
import { ProjectService } from 'src/app/components/project/project.service';
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
    project: any

    totalRecords: any;
    page: number = 1

    constructor(private allocationService: AllocationService, private router: ActivatedRoute, private projectService: ProjectService) { }

    ngOnInit(): void {
        this.allocationService.readSkills().subscribe(skills => {
            this.skills = skills;
        })
        this.allocationService.read().subscribe(employees => {
            this.employees = employees;
            this.totalRecords = employees.length;
        })
        const id = this.router.snapshot.paramMap.get('id');
        this.projectService.readByPk(id).subscribe(project => {
            this.project = project;
        })
    }
}
