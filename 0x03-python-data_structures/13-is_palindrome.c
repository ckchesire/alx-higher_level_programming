#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverse singly linked listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: address of the new head of reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *previous = NULL, *next = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}
/**
 * is_palindrome - function that checks if a singly list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: '0' if it is not a palindrome, '1' if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_pt = *head, *fast_pt = *head, *first_half = *head;
	listint_t *second_half, *reversed_second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast_pt != NULL && fast_pt->next != NULL)
	{
		slow_pt = slow_pt->next;
		fast_pt = fast_pt->next->next;
	}

	second_half = reverse_list(&slow_pt);
	reversed_second_half = second_half;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			reverse_list(&reversed_second_half);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverse_list(&reversed_second_half);
	return (1);
}
