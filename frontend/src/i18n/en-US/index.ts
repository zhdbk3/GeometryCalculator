import docs from './docs.md?raw';
import about from './about.md?raw';

export default {
  markdown: {
    docs: () => docs,
    about: () => about,
  },
};
