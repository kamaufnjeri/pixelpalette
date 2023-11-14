# Pixelpallete.
Pixelpallete is designed to connect artists with art enthusiasts. It serves as a marketplace for artists to showcase their masterpieces while providing a seamless experience for art lovers to explore, interact, and purchase their favorite art pieces.

[Visit our website](https://kamaufnjeri.github.io)

## Authors
* **Florence Njeri Kamau**
  - [Github](https://github.com/kamaufnjeri)
  - [LinkedIn](https://www.linkedin.com/in/florence-kamau-696874241/)
* **Uel Kariuki**
  - [Github](https://github.com/uelkariuki)
  - [LinkedIn](https://www.linkedin.com/in/uel-kariuki/)
* **Abraham Bett**
  - [Github](https://github.com/abraham-ship)
  - [LinkedIn](https://www.linkedin.com/in/abraham-bett-006245199/)

## Installation
* In your temirnal eg. Ubuntu terminal run the following command `git clone https://github.com/kamaufnjeri/pixelpallete.git`
* Go into the projects directory by running the command `cd pixelpallete`
* Create a virtual enviromnent by the command `virtualenv name-of-your-virtual-enviroment`. To install virtual environment use `sudo apt install virtualenv`
* To activate the virtual environment. For linux run the command `source name-of-your-virtual-environment/bin/activate` and windows `source name-of-your-virtual-environment/Scripts/activate`
* Then run the command `pip install -r requirements.txt` to install the libraries and modules needed by pixelpallete
* Run the command `python app.py` or `python3 app.py` to run pixelpallete
* To access pixelpallete open the url `http://127.0.0.0.1:5000`

## Features
* Artist Showcases: Artists can create profiles and exhibit their best artworks, providing a portfolio for potential buyers.
* Artwork Categorization and Search: Enables easy browsing and discovery through categorization and search functionalities.
* User-Friendly Interface: Offers an intuitive and visually appealing platform for a delightful user experience.

## Usage
1. Signup/Login:<br>
For the best experience, you will need to login or signup. You can do that by clicking on either the signup or login button:<br>
![Signup/Login](screenshots/home.jpg)<br>
If you are signing up, you have the option to choose to either sign up as an artist or an art enthusiast:<br>
![Signup](screenshots/sign.jpg)<br>

2. Explore Artworks:<br>
Visit the website and start exploring the diverse range of art showcased by talented artists.<br>
![Explore the page](screenshots/art.jpg)<br>

3. Artist Interaction:<br>
You can filter by categories provided and click on them to view individual arts.<br>
![Interacting with arts](screenshots/search.jpg)<br>

4. Uploading art:<br>
As an artist you will be able to upload your media along with a description and price tag to the platform. Just click on the hamburger button on the top left of your screen and choose to `Add An Artwork`<br>
![Uploading media](screenshots/upl.jpg)

5. Adding to favorites:<br>
If you find an art piece you love, view the art and add it to your favorites cart(highlighted).<br>
![Purchasing items](screenshots/cart.jpg)<br>
Your items will appear in your cart.To purchase an artwork one needs to contact the owner<br>
![Cart](screenshots/cart.png)<br>

6. Add exhibitions:<br>
As an artist, you might want to exhibit your work on the platform and you can do that by clicking on the hamburger button on the top left of your sccreen and selecting `Create An Exhibit`:<br>
You then need name your exhibition and specify for how long you want the exhibit to run.<br>
![Creating an exhibit](screenshots/create.jpg)<br>
After that you need to add you artwork to the exhibit by visiting your `My Artworks` page and choosing from your artworks the artworks you wish to add to the exhibit<br>
![Adding art to exhibit](screenshots/exhibit.jpg)<br>
You should see it appear in the Exhibits section of your page.<br>
![Exhibits](screenshots/count.jpg)<br>
Additionally you can choose to have an artwork exclusively as an exhibit artwork by choosing `exhibit artwork` option and by going to my artworks you can then add it to exhibits, such artworks will only be available in the exhibit. After the exhibit you can choose to add it to the general artwork.<br>
![Uploading to exhibit](screenshots/ty.jpg)<br>

7. Discover Artists:<br>
You can be able to see all artists by visiting the artists page where you can view all artworks of a specific artist.<br>
![Artists page](screenshots/artists.jpg)<br>

## Technologies used
* HTML, CSS, JavaScript for frontend development.
* Python for server-side implementation.
* Flask the Web Development Framework.
* Additional libraries and frameworks may have been used. Details can be found in the code repository.

## Acknowledgment
* [ALX](https://www.alxafrica.com/) - software engineering.
* **Florence Njeri Kamau** - [@kamaufnjeri](https://github.com/kamaufnjeri) for the inspiration.

## Contributions

We welcome contributions from the community to improve PixelPallete. To contribute, please follow these steps:

1. **Fork the Repository:** Start by forking the repository to your GitHub account.

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. **Clone the Repository:** Clone the forked repository to your local machine.

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

3. **Create a Branch:** Create a new branch for your feature or bug fix using a descriptive branch name.

    ```bash
    git checkout -b feature/new-feature
    ```

4. **Make Changes:** Implement your changes or add new features. Ensure that your code follows the project's coding standards.

5. **Test Locally:** Test your changes locally to make sure they work as expected.

6. **Commit Changes:** Commit your changes with a clear and concise commit message.

    ```bash
    git commit -m "Add new feature: your feature description"
    ```

7. **Push Changes:** Push your changes to your forked repository on GitHub.

    ```bash
    git push origin feature/new-feature
    ```

8. **Create Pull Request:** Open a pull request on the original repository. Provide a clear and detailed description of your changes.

9. **Code Review:** The maintainers will review your code, suggest changes if needed, and discuss any necessary modifications.

10. **Merge:** Once your changes are approved, they will be merged into the main branch.

### Example Contribution

Here's an example of a contribution that fixes a bug:

1. Fork the repository to your GitHub account.

2. Clone the forked repository to your local machine.

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

3. Create a branch for the bug fix.

    ```bash
    git checkout -b bugfix/fix-description
    ```

4. Make the necessary changes to fix the bug.

5. Test the changes locally to ensure the bug is resolved.

6. Commit the changes.

    ```bash
    git commit -m "Fix: Describe the bug that was fixed"
    ```

7. Push the changes to your forked repository.

    ```bash
    git push origin bugfix/fix-description
    ```

8. Create a pull request with a detailed description of the bug and the fix.

9. Participate in the code review process and make any required adjustments.

10. Once approved, the changes will be merged into the main branch.

Thank you for contributing to PixelPallete!

## Related Projects
1. **Art Gallery Management System**
   - GitHub: [Art Gallery Management](https://github.com/roshan02/Art-Gallery-Management-System)
   - Description: Keeps record of artists, their paintings, art gallery details, exhibition details and showcases pictures of paintings to the customers.
  
2. **Web umenia**
   - GitHub: [Web umenia](https://github.com/SlovakNationalGallery/webumenia.sk)
   - Description: Web umenia is an open platform to explore digitized art collections from public galleries and museums.
